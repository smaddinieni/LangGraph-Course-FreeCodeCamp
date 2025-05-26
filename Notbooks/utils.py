import os
import getpass
import requests
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional, Union, TypedDict
from tools import *
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph

load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# LLm models
model4omini = init_chat_model(
    "gpt-4.1-mini-2025-04-14", model_provider="openai", temperature=0, max_tokens=2048
)
model25flash = init_chat_model(
    "gemini-2.5-flash-preview-05-20",
    model_provider="google_genai",
    temperature=0,
    max_tokens=2048,
)

# React agents
openaiagent = create_react_agent(
    model=model4omini, tools=[], prompt="You are an helpful AI assistant"
)

openai_websearch_agent = create_react_agent(
    model=model4omini,
    tools=[{"type": "web_search_preview"}],
    prompt="You are an helpful AI assistant",
)

geminiagent = create_react_agent(
    model=model25flash, tools=[], prompt="You are an helpful AI assistant"
)

gemini_websearch_agent = create_react_agent(
    model=model25flash, tools=[tavily_search], prompt="You are an helpful AI assistant"
)
