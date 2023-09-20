from fastapi import APIRouter
from .utils import SentimentalEntry
from .utils import SentimentalModel
from .utils import ResponseTo

import logging
log = logging.getLogger("roberta_model")

router = APIRouter(prefix="/api/v1/roberta")


def format_roberta(data: list, index: int):
    response = ResponseTo()
    output = list()

    if data[0].get('label') == 'hate':
        output.append(
            {"label": "HATE", "model": "facebook/roberta-hate-speech-dynabench-r4-target", "score": data[0].get('score'), "index": index})
    else:
        output.append(
            {"label": "NO_HATE", "model": "facebook/roberta-hate-speech-dynabench-r4-target", "score": data[0].get('score'), "index": index})

    response.code = "OK"
    response.message = ""
    response.value = output

    return response


@router.post("/predict/")
def create_roberta_model(entry: SentimentalEntry) -> dict:
    try:
        sentimental = SentimentalModel(
            name="facebook/roberta-hate-speech-dynabench-r4-target")
        sentimental.description = "Descripcion"
        sentimental.predict(entry.data[0],entry.data[1], format_roberta)

        return sentimental.prediction.__dict__
    except BaseException as ex:
        log.error(msg=str(ex), exc_info=ex)
        return ResponseTo(code=500, message=str(ex)).__dict__
