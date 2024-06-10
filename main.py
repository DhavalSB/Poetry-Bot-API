from fastapi import FastAPI
from geminiInterface import *

app = FastAPI()

@app.get("/daily-prompt")
async def returnDailyPrompt():
    return {"Message": dailyPrompt()}
