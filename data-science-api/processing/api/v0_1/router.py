"""
Define the routes of the API
"""

import api.v0_1.endpoints

from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(api.v0_1.endpoints.router)
