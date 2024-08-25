import textwrap
from fastapi import APIRouter
from IPython.display import Markdown
from model import model

router = APIRouter()

@router.get('/gen/report')
def get_report(content:str, title:str, format:str, count:int, tone:str):

    content = model.generate_content(f"""Here is the content:{content}, Please extract all 
                                     content from the provided scraped data that is relevant 
                                     to the title: {title}. 
                                     Focus on the main points and key details that directly 
                                     relate to this title. After extracting the relevant content, 
                                     generate a report with a word count of {count}. 
                                     write a {format} report with a {tone} tone. 
                                     Remove any unnecessary or extraneous content 
                                     such as links or unrelated details""")
    return {"report": content.text}

@router.get('/gen/summary')
def get_sum(content:str, title:str, count:int):

    content = model.generate_content(f"""Here is the content:{content} Please extract all content from the provided 
                                     scraped data that is relevant to the title: {title}. 
                                     Focus on the main points and key details that directly relate 
                                     to this title. After extracting the relevant content, 
                                     generate a summary with a word count of {count}. 
                                     Remove any unnecessary or extraneous content such as links or 
                                     unrelated details.""")
    return {"summary": content.text}

@router.get('/gen/bullets')
def get_bullets(content:str, title:str, count:int):
   
    content = model.generate_content(f"""Here is the content:{content} Please extract all content from the provided scraped 
                                     data that is relevant to the title: {title}. 
                                     Focus on the main points and key details that directly relate 
                                     to this title. After extracting the relevant content, 
                                     generate {count} bullet points that clearly 
                                     summarize the key information. Remove any unnecessary or 
                                     extraneous content such as links or unrelated details.""")
    return {"bullets": content.text}

@router.get('/get/story')
def get_story(count:int, genre:str, setting:str, perspective:str, tone:str):

    content = model.generate_content(f"""Please generate a {count} word story in the {genre} genre. 
                                     Ensure the story has a {tone} tone and 
                                     is written from a {perspective} point of view. 
                                     Set the story in {setting} Remove any extraneous content, 
                                     such as links or unrelated details, to maintain focus and clarity.""")
    return {"story": content.text}
