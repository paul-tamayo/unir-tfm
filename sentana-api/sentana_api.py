from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from routers.utils import ResponseTo
import routers.byt5_model as bty5_model
import routers.bert_model as bert_model
import routers.nltk_model as nltk_model
import routers.roberta_model as roberta_model
import uvicorn

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)
app.include_router(bert_model.router)
app.include_router(bty5_model.router)
app.include_router(nltk_model.router)
app.include_router(roberta_model.router)


@app.get("/api/v1/health")
async def get_health() -> dict:
    try:
        return {'API': "Analizador de Sentimiento", "Versión": "1.0.0"}
    except BaseException as ex:
        return ResponseTo(code=500, message=str(ex)).__dict__

if __name__ == "__main__":
    uvicorn.run("sentana_api:app", host="127.0.0.1", port=8000, reload=True)
