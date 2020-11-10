from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

class FeedbackData(BaseModel):
    profileId: str
    eventId: str
    message: str	

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/analysis/")
async def analysis(fbd: FeedbackData):
    vs = analyzer.polarity_scores(fbd.message)
    rs = jsonable_encoder(vs)
    return rs
