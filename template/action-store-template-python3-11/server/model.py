"""This module defines models used by FastAPI."""
from typing import Optional, Dict, Any

from pydantic import BaseModel


class RequestModel(BaseModel):
    """Define a request model."""

    action: str
    input:  Optional[Any] = {}
    secrets: Optional[Dict] = {}
    runner: Optional[str]


class ResponseModel(BaseModel):
    """Define a response model."""

    data: dict
