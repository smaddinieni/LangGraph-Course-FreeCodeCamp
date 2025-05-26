import os
import getpass
from dotenv import load_dotenv

load_dotenv()
from tavily import TavilyClient


def tavily_search(query: str) -> dict:
    """
    Search for information using the Tavily API.

    Args:
        query (str): The search query string.

    Returns:
        dict: The search results from Tavily.
    """
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        api_key = getpass.getpass("Enter Tavily API key: ")
        os.environ["TAVILY_API_KEY"] = api_key
    client = TavilyClient(api_key=api_key)
    return client.search(query)
