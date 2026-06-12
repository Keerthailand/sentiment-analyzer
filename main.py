from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from model import analyze_sentiment

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/analyze")
def analyze(input: TextInput):
    if not input.text.strip():
        return {"error": "No text provided"}
    results = analyze_sentiment(input.text)
    return {"results": results}