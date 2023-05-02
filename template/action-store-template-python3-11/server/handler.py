"""This module defines how requests are handled by the server."""
import traceback
from typing import Any

from fastapi.concurrency import run_in_threadpool

import kubiya
from kubiya.action_store import ActionStore
from kubiya.loader import get_single_action_store

from . import model


VERSION = "1.0.0"
RUNTIME = f"python3.11-runner-{VERSION}"

class SecretNotFoundError(Exception):
    pass

class SecretsDict(dict):
    def __getitem__(self,key):
        try:
            return super(SecretsDict, self ).__getitem__( key )
        except KeyError as e:
            raise SecretNotFoundError(f"Secret '{key}' not found")

def execute_handler(request: model.RequestModel, action_store: ActionStore) -> Any:
    try:
        if request.action == '__KUBIYA_DISCOVER__':
            icon_url = getattr(action_store, "icon_url", None)

            return {
                "faas_runtime": RUNTIME,
                "name": action_store.get_name(),
                "version": action_store.get_version(),
                "registered_actions": action_store.get_registered_actions(),
                "secrets": action_store.get_registered_secrets(),
                "kubiya_version": "python-sdk: " + kubiya.__version__,
                "actions_metadata": action_store._action_metadata,
                "icon_url": icon_url,
                
            }

        if request.secrets:
            setattr(action_store, "secrets", SecretsDict(**request.secrets))
        else:
            setattr(action_store, "secrets", SecretsDict())
        result = action_store.execute_action(request.action, request.input)
        return {"result": result, "faas_runtime": RUNTIME}
    except Exception as e:
        return {
            "error": str(e),
            "stacktrace": traceback.format_exc(),
        }
