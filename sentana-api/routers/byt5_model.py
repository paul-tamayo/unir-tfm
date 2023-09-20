from fastapi import APIRouter
from transformers import AutoTokenizer, T5ForConditionalGeneration

from .utils import SentimentalEntry
from .utils import ResponseTo

import logging
log = logging.getLogger("bty5_model")

router = APIRouter(prefix="/api/v1/bty5")

ckpt = 'Narrativa/byt5-base-tweet-hate-detection'
tokenizer = AutoTokenizer.from_pretrained(ckpt)
model = T5ForConditionalGeneration.from_pretrained(ckpt)


def classify_tweet(tweet):
    inputs = tokenizer([tweet], padding='max_length',
                       truncation=True, max_length=512, return_tensors='pt')
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def create_response(data: list) -> ResponseTo:
    response = ResponseTo()
    output = list()

    predict = classify_tweet(data[0])

    if predict == 'hate-speech':
        output.append(
            {"label": "HATE", "model": "Narrativa/byt5-base-tweet-hate-detection", "score": "N/A", "index": data[1]})
    else:
        output.append(
            {"label": "NO_HATE", "model": "Narrativa/byt5-base-tweet-hate-detection", "score": "N/A", "index": data[1]})

    response.code = "OK"
    response.message = ""
    response.value = output

    return response


@router.post("/predict/")
def create_bty5_model(entry: SentimentalEntry) -> dict:
    try:
        return create_response(entry.data).__dict__
    except BaseException as ex:
        log.error(msg=str(ex), exc_info=ex)
        return ResponseTo(code=500, message=str(ex)).__dict__
