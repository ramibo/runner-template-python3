"""This module defines models used by FastAPI."""
from typing import Optional, Dict, Any

from pydantic import BaseModel


class RequestModel(BaseModel):
    """Define a request model."""

    action: Optional[str]
    input:  Optional[Any]
    secrets: Optional[Dict]
    action_store: Optional[str]
    inbox_id: Optional[str]
    runner: Optional[str]


class ResponseModel(BaseModel):
    """Define a response model."""

    data: dict
