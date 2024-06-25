from fastapi import FastAPI
from geminiInterface import *
from selectPrompt import *

app = FastAPI()

@app.get("/daily-prompt")
async def returnDailyPrompt():
    return selectPrompt()
