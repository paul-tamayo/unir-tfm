from fastapi import APIRouter
from .utils import SentimentalEntry
from .utils import SentimentalModel
from .utils import ResponseTo

import logging
log = logging.getLogger("bert_model")

router = APIRouter(prefix="/api/v1/bert")


def format_bert(data: list, index: int):
    response = ResponseTo()
    output = list()

    if data[0].get('label') == 'NEG':
        output.append(
            {"label": "HATE", "model": "finiteautomata/bertweet-base-sentiment-analysis", "score": data[0].get('score'), "index": index})
    else:
        output.append(
            {"label": "NO_HATE", "model": "finiteautomata/bertweet-base-sentiment-analysis", "score": data[0].get('score'), "index": index})

    response.code = "OK"
    response.message = ""
    response.value = output

    return response


@router.post("/predict/")
def create_bert_model(entry: SentimentalEntry) -> dict:
    try:
        sentimental = SentimentalModel(
            name="finiteautomata/bertweet-base-sentiment-analysis")
        sentimental.description = "Descripcion"
        sentimental.predict(entry.data[0],entry.data[1], format_bert)

        return sentimental.prediction.__dict__
    except BaseException as ex:
        log.error(msg=str(ex), exc_info=ex)
        return ResponseTo(code=500, message=str(ex)).__dict__
