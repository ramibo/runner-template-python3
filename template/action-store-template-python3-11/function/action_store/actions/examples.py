import time

import logging
from pydantic import BaseModel
from typing import Optional, List, Dict
from . import actionstore as action_store

logging.basicConfig(level=logging.INFO)

# The action store definition is declared in the __init__.py file
# This is the main file that is executed when the action store is deployed

# This is a simple action that returns a string
# It is not validated, so you can pass anything as an input
@action_store.kubiya_action(validate_input=True)
def simple_action(input):
    """ foo"""
    logging.info("Got input: %s", input)
    return "Hello from simple_action! Recieved input: " + str(input)

# This is an example model, you can use it to validate your input
# And build amazing user interfaces in the Kubiya no-code platform
class ExampleModel(BaseModel):
    """used for type hints, automatic decumentation and validation"""
    required_string: str
    optional_string: Optional[str] = None
    required_int: int
    optional_int: Optional[int] = None

# This is a simple action that requires a model as input
# It is validated, so you can only pass a model that matches the ExampleModel
# It will also be documented in the Kubiya no-code platform
@action_store.kubiya_action(validate_input=True)
def action_with_model(user: ExampleModel) -> str:
    logging.info("Got user: %s", user)
    """returns baz"""
    return "Hello from action_with_model! Recieved input: " + str(user)
