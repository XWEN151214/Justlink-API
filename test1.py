import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")
soup = BeautifulSoup(response.content, 'html.parser')
body = soup.find('body').text.strip()
print(body)