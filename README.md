#Import below libraries

import asyncio
import os

from agent_framework import (
    Agent
)
from agent_framework.azure import AzureOpenAIResponsesClient
from agent_framework.orchestrations import MagenticBuilder
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
from agent_framework.devui import serve

------------------------------------------------

python final.py 
