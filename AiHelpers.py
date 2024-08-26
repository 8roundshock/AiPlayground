import os
import asyncio
import base64
from openai import OpenAI
from playwright.sync_api import sync_playwright
from langchain_openai import ChatOpenAI
from AiClass import *
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatOpenAI model with specific parameters
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=os.environ['OPEN_AI_APIKEY'])

# Wrap the LLM to provide structured output
structured_llm = llm.with_structured_output(DocumentMetaData)

def getWebPage(url):
    """
    Fetches a webpage, takes a screenshot, and encodes the image to base64.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: Base64 encoded string of the screenshot.
    """
    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to the specified URL
        page.goto(str(url))
        # Take a screenshot of the entire page
        page.screenshot(path="screenshot.png", full_page=True)
        browser.close()
        # Encode the screenshot to base64
        return encodeImage(image_path)

# Path to the screenshot image
image_path = 'screenshot.png'

def encodeImage(image_path):
    """
    Encodes an image to a base64 string.

    Args:
        image_path (str): The file path of the image to encode.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        # Read the image file and encode it to base64
        return base64.b64encode(image_file.read()).decode('utf-8')

def searchForData(base64_image):
    """
    Sends a base64 encoded image to the LLM to extract data.

    Args:
        base64_image (str): Base64 encoded string of the image.

    Returns:
        dict: The structured data extracted by the LLM.
    """
    message = HumanMessage(
        content=[
            {"type": "text", "text": "Extract data from this screenshot"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ],
    )
    # Invoke the LLM with the message and return the structured output
    return structured_llm.invoke([message])