from pydantic import BaseModel
from transformers import pipeline
from typing import Any


class ResponseTo():
    code: str
    message: str
    value: Any

    def __init__(self, code: str = None, message: str = None) -> None:
        self.code = code
        self.message = message


class SentimentalEntry(BaseModel):
    data: list


class SentimentalModel():
    name: str
    description: str
    prediction: ResponseTo

    def __init__(self, name: str, description: str = None) -> None:
        self.name = name
        self.description = description

    def predict(self, data: str, index: int, format_output):
        sentimental_pipeline = pipeline(model=self.name)
        self.prediction = format_output(sentimental_pipeline(data), index)
