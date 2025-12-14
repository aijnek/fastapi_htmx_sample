from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests


templates = Jinja2Templates(directory="templates")

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gpt-oss:20b"


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request}
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate_response(prompt: str = Form()):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        generated_text = response.json()["response"]
    else:
        generated_text = "エラーが発生しました。"
    
    return f"<div>{generated_text}</div>"