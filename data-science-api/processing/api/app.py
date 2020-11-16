"""Configuração da API usando a biblioteca FastAPI
"""


from fastapi import FastAPI
from api.v0_1.router import api_router

tags_metadata = [
    {
        "name": "<Nome-API>",
        "description": "A<descrever o que trata a api - exemplo para o template data-science-api>",
    },
]


app = FastAPI(
    title="<Nome-API>",
    description="<descrever o que trata a api - exemplo para o template data-science-api>",
    version="0.1",
    openapi_tags=tags_metadata,
)
app.include_router(api_router)
