📝 Multi-Agent Workflow – Notes
🔹 Purpose
Build a multi-agent content pipeline
Uses Azure AI + agent_framework
Orchestrated using Magentic workflow
UI available via DevUI
🔹 Key Components
1. Environment Setup
Uses .env file
Required variables:
AZURE_AI_PROJECT_ENDPOINT
AZURE_AI_MODEL_DEPLOYMENT_NAME
Auth via AzureCliCredential
2. Client Creation
AzureOpenAIResponsesClient used
Shared across all agents
Created via a factory function (create_client())
🔹 Agents Overview
✍️ Writer Agent
Generates initial content
Focus: clarity + structure
🔍 Reviewer Agent
Evaluates content
Returns structured JSON:
score
feedback
clarity, completeness, accuracy, structure
✏️ Editor Agent
Improves content using feedback
📰 Publisher Agent
Formats content professionally
📊 Summarizer Agent
Creates final summary/report
🧠 Manager Agent
Controls workflow
Coordinates all agents
🔹 Workflow (Magentic)
Built using MagenticBuilder
Participants:
Writer → Reviewer → Editor → Publisher → Summarizer
Controlled by Manager Agent
Config:
max_round_count = 10
max_stall_count = 3
max_reset_count = 2
intermediate_outputs = False
🔹 Execution Flow
User gives input
Writer creates content
Reviewer evaluates
Editor improves
Publisher formats
Summarizer generates report
Manager ensures flow completion
🔹 Dev UI
Runs on: http://localhost:8093

Enabled using:

serve(entities=[workflow], port=8093)
Purpose:
Visualize workflow
Debug agent interactions
Provide inputs
🔹 Important Concepts
Multi-Agent Collaboration
LLM Orchestration
Structured Output (Pydantic)
Feedback Loop System
Azure AI Integration
🔹 Common Issues
Serialization errors → avoid custom objects (like Message)
Missing env vars → check .env
Auth issues → run az login
🔹 Use Cases
Content generation pipelines
AI review systems
Automated report generation
Multi-step LLM workflows
