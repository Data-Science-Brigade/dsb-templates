import api.v0_1
import random

from api.v0_1.models import DocumentModel, DocumentOutputModel

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional

router = APIRouter()


@router.post("/example_endpoint", response_model=List[DocumentOutputModel])
async def example_endpoint(doc: DocumentModel):
    """This is just a template for an endpoint, remove it once you start working on the endpoints
    """
    raise NotImplementedError()
