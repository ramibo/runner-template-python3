import sys
from pathlib import Path
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import kubiya

# This is the action store object
# It is used to define the action store name and version
# It will get passed to the Kubiya platform and used to identify the action store

# Do not forget to change the action store name according to the name you'll use to bundle it
action_store = kubiya.ActionStore("sample-action-store", "0.1.0")

# This is a simple action that returns a string
# It is not validated, so you can pass anything as an input
@action_store.kubiya_action(validate_input=True)
def simple_action(input):
    """returns foo"""
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
    """returns baz"""
    return "Hello from action_with_model! Recieved input: " + str(user)
