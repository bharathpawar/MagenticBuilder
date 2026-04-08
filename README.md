Multi-Agent Content Workflow using Azure AI
Overview

This project demonstrates a multi-agent orchestration system built using the agent_framework and Azure AI. It simulates a real-world content production pipeline where multiple AI agents collaborate to:

Generate content
Review quality
Improve based on feedback
Format for publishing
Summarize the workflow

The system is orchestrated using a Magentic workflow and can be interacted with via a local Dev UI.

Architecture

The workflow consists of the following agents:

Writer Agent
Generates structured content based on user input.
Reviewer Agent
Evaluates content and returns structured feedback:
Score (1–10)
Clarity
Completeness
Accuracy
Structure
Editor Agent
Improves the content using reviewer feedback.
Publisher Agent
Formats content professionally with headings and structure.
Summarizer Agent
Produces a concise report of the workflow and final output.
Manager Agent
Orchestrates the entire workflow using Magentic coordination.
Features
Multi-agent collaboration
Structured output validation using Pydantic
Azure AI integration
Interactive Dev UI
Configurable orchestration limits (rounds, stalls, resets)
Prerequisites
Python 3.9+
Azure subscription
Azure CLI installed and authenticated
Installation
Clone the repository:
git clone <your-repo-url>
cd <your-repo-folder>
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory and add:

AZURE_AI_PROJECT_ENDPOINT=<your_project_endpoint>
AZURE_AI_MODEL_DEPLOYMENT_NAME=<your_model_deployment>
Authentication

Login to Azure CLI:

az login

The project uses:

AzureCliCredential()
Running the Application

Start the application:

python main.py
Access Dev UI

Once the app is running, open:

http://localhost:8093

This UI allows you to:

Interact with the workflow
Provide prompts
Observe agent collaboration
Workflow Configuration

The orchestration is configured with:

max_round_count=10
max_stall_count=3
max_reset_count=2

You can tweak these values based on your use case.

Project Structure
.
├── main.py
├── .env
├── requirements.txt
└── README.md
Example Use Case

Input:

Write an article about AI in healthcare

Workflow:

Writer generates content
Reviewer scores it
Editor improves it
Publisher formats it
Summarizer creates final report
Troubleshooting
Common Issues
Authentication Error
Ensure az login is completed
Environment Variables Missing
Verify .env file is correctly configured
Serialization Errors
Ensure all outputs are JSON serializable
Avoid passing unsupported types like custom classes directly
Future Enhancements
Add memory between agents
Integrate external tools (search, databases)
Support streaming outputs
Deploy as a web service
License

This project is for educational and experimental purposes.
