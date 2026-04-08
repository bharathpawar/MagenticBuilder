import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel

from azure.identity import AzureCliCredential

from agent_framework import Agent
from agent_framework.azure import AzureOpenAIResponsesClient
from agent_framework.orchestrations import MagenticBuilder
from agent_framework.devui import serve
from agent_framework._types import Message


    # Load environment variables
load_dotenv()


# -----------------------------
# Structured Output
# -----------------------------
class ReviewResult(BaseModel):
    score: int
    feedback: str
    clarity: int
    completeness: int
    accuracy: int
    structure: int


def main():

    credential = AzureCliCredential()

    project_endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
    deployment = os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]

    # -----------------------------
    # Client factory
    # -----------------------------
    def create_client():
        return AzureOpenAIResponsesClient(
            project_endpoint=project_endpoint,
            deployment_name=deployment,
            credential=credential,
        )

    # -----------------------------
    # Writer Agent
    # -----------------------------
    writer_agent = Agent(
        name="WriterAgent",
        description="Creates high quality content",
        instructions=(
            "You are a professional content writer. "
            "Create clear and structured content for the user's request."
        ),
        client=create_client(),
    )

    # -----------------------------
    # Reviewer Agent
    # -----------------------------
    reviewer_agent = Agent(
        name="ReviewerAgent",
        description="Reviews content quality",
        instructions=(
            "Return a JSON response with these fields: score (1-10), feedback (string), "
            "clarity (1-10), completeness (1-10), accuracy (1-10), structure (1-10)"
        ),
        client=create_client(),
    )

    # -----------------------------
    # Editor Agent
    # -----------------------------
    editor_agent = Agent(
        name="EditorAgent",
        description="Improves content using feedback",
        instructions=(
            "Improve the content using reviewer feedback while maintaining original intent."
        ),
        client=create_client(),
    )

    # -----------------------------
    # Publisher Agent
    # -----------------------------
    publisher_agent = Agent(
        name="PublisherAgent",
        description="Formats content for publishing",
        instructions=(
            "Format the content professionally with headings and structure."
        ),
        client=create_client(),
    )

    # -----------------------------
    # Summarizer Agent
    # -----------------------------
    summarizer_agent = Agent(
        name="SummarizerAgent",
        description="Creates final report",
        instructions=(
            "Create a concise publication report summarizing the final content and workflow path."
        ),
        client=create_client(),
    )

    # -----------------------------
    # Manager Agent
    # -----------------------------
    manager_agent = Agent(
        name="MagenticManager",
        description="Orchestrates the workflow",
        instructions="Coordinate the team to complete the task efficiently.",
        client=create_client(),
    )

    print("\nBuilding Magentic Workflow...")

    # -----------------------------
    # Build Magentic workflow
    # -----------------------------
    workflow = MagenticBuilder(
        participants=[
            writer_agent,
            reviewer_agent,
            editor_agent,
            publisher_agent,
            summarizer_agent,
        ],
        manager_agent=manager_agent,
        intermediate_outputs=False,
        max_round_count=10,
        max_stall_count=3,
        max_reset_count=2,
    ).build()

    # -----------------------------
    # Launch DevUI
    # -----------------------------
    print("Launching DevUI at http://localhost:8093")

    serve(
        entities=[workflow],
        port=8093,
        auto_open=True,
    )


if __name__ == "__main__":
    main()