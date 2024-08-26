import requests
from bs4 import BeautifulSoup
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

response = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")
soup = BeautifulSoup(response.content, 'html.parser')
body = soup.find('body').text.strip()
API_KEY = "
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")
content = model.generate_content(f"Here is the content of the blog/article: {body}, Please analyze the following blog/article content and generate a concise and effective report. Focus on summarizing the key points, insights, and main arguments presented. Exclude any extraneous information, such as hyperlinks, advertisements, unrelated sections, or promotional content. Ensure the report is well-organized, clear, and captures the essence of the original content without any unnecessary details.")
print(content.text)
