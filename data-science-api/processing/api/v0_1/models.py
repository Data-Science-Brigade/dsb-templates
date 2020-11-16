""" JSON objects used in the API
"""

from enum import Enum

from pydantic import BaseModel, Field
from typing import Optional


class DocumentModel(BaseModel):
    # TODO: This is just a template, remove this class when you start working on the models
    tipo_documento: str = Field(..., example="doc")
    conteudo_documento: Optional[str] = Field(None, example="")
    link_documento: Optional[str] = Field(None, example="")


class DocumentOutputModel(BaseModel):
    # TODO: This is just a template, remove this class when you start working on the models
    tipo_documento: str = Field(..., example="doc")
    link_documento: str = Field(..., example="")
    similaridade: float = Field(..., example=0.9)
