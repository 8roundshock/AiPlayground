import os
import asyncio
from AiHelpers import *

# URL of the webpage to fetch
content = 'https://data.nasa.gov/dataset/SASSIE-Arctic-Field-Campaign-PALS-Data-Fall-2022/57hc-rkhv/about_data'

# Fetch the webpage and take a screenshot, returning the base64 encoded image
webPage = getWebPage(content)

# Print the structured data extracted from the screenshot
print(searchForData(webPage))