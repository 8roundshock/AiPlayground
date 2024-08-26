import os
import asyncio
import base64
from openai import OpenAI
from playwright.sync_api import sync_playwright
from langchain_openai import ChatOpenAI
from AiClass import *
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0 ,model="gpt-4o-mini",api_key=os.environ['OPEN_AI_APIKEY'])

structured_llm = llm.with_structured_output(DocumentMetaData)

def getWebPage(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(str(url))
        page.screenshot(path="screenshot.png", full_page=True)
        browser.close()
        return encodeImage(image_path)

image_path = 'screenshot.png'

def encodeImage(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def searchForData(base64_image):
    message = HumanMessage(
    content=[
        {"type": "text", "text": "Extract data from this screenshotß"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ],
    )
    return structured_llm.invoke([message])