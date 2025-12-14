from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
import httpx
import json


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


@app.get("/generate")
async def generate_response(prompt: str = Query(...)):
    async def generate_stream():
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": True
        }

        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                async with client.stream('POST', OLLAMA_URL, json=payload) as response:
                    async for line in response.aiter_lines():
                        if line.strip():
                            data = json.loads(line)
                            chunk = data.get("response", "")
                            if chunk:
                                # SSE形式で送信
                                yield f"data: {chunk}\n\n"

                            # Ollamaのストリーミング完了を検出
                            if data.get("done", False):
                                break
        except Exception as e:
            yield f"data: エラーが発生しました: {str(e)}\n\n"

    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream"
    )