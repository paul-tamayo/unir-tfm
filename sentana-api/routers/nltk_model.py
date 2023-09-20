from fastapi import APIRouter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


from .utils import SentimentalEntry
from .utils import ResponseTo

import nltk
import logging
log = logging.getLogger("nltk_model")

router = APIRouter(prefix="/api/v1/nltk")
nltk.download('vader_lexicon')


def create_response(data: list) -> ResponseTo:
    output = list()
    response = ResponseTo()
    sid = SentimentIntensityAnalyzer()

    predict = sid.polarity_scores(data[0])
    a = predict.get('neg')
    b = predict.get('neu')
    c = predict.get('pos')
    negativo = (a >= b or a > c)
    if negativo:
        output.append({"label": "HATE", "model": "NLKT", "score": a, "index": data[1]})
    else:
        output.append(
            {"label": "NO_HATE", "model": "NLKT", "score": (b+c), "index": data[1]})

    response.code = "OK"
    response.message = ""
    response.value = output

    return response


@router.post("/predict/")
def create_nltk_model(entry: SentimentalEntry) -> dict:
    try:
        return create_response(entry.data).__dict__
    except BaseException as ex:
        log.error(msg=str(ex), exc_info=ex)
        return ResponseTo(code=500, message=str(ex)).__dict__
