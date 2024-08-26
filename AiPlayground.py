import os
import asyncio
from AiHelpers import *

content = 'https://data.nasa.gov/dataset/SASSIE-Arctic-Field-Campaign-PALS-Data-Fall-2022/57hc-rkhv/about_data'

webPage = getWebPage(content)

print (searchForData(webPage))