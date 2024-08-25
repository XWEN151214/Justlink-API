import requests
from fastapi import APIRouter
from bs4 import BeautifulSoup

router = APIRouter()

@router.get('/get-content')
def get_content(link:str):

    if link:
        if not link.startswith('https://'):
            link = 'https://' + link
        try:
    
            response = requests.get(f"{link}")
        except Exception as e:
            
            return {"Error": e}
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text.strip()
        body = soup.body
        for a in body.find_all('a'):
            a.decompose()
        body = body.text.strip()
        return {"content": body, "title": title}
    return {"Error": "Undefined Link"}