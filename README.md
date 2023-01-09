# runner-template-python3


## Downloading the templates

Using template pull with the repository's URL:

```bash
faas-cli template pull https://github.com/kubiyabot/runner-template-python3
```


Using your `stack.yml` file:

```yaml
configuration:
    templates:
        - name: runner-template-python3
functions:
  action-store-aws:
    lang: python3-k-runner
    handler: ./action-store-directory
    image: your-registry/your-runner:latest
    secrets:
      - acrd
    annotations:
        topic: "stores.action-store-name"
```

# Using the runner-template-python3 templates

Create a new function

```
export OPENFAAS_PREFIX=yourRegistryPrefix
export FN="tester"
faas-cli new --lang runner-template-python3 $FN
```

Build, push, and deploy

```
faas-cli up -f $FN.yml
```

Test the new function

```
echo -n content | faas-cli invoke $FN
```

## Event and Context Data

The function handler is passed two arguments, *event* and *context*.

*event* contains data about the request, including:
- body
- headers
- method
- query
- path

*context* contains basic information about the function, including:
- hostname

## Response Bodies

By default, the template will automatically attempt to set the correct Content-Type header for you based on the type of response.

For example, returning a dict object type will automatically attach the header `Content-Type: application/json` and returning a string type will automatically attach the `Content-Type: text/html, charset=utf-8` for you.

## Example usage

### in function/main_store.py you'll find a sample-store and actions

```python
action_store = kubiya.ActionStore("sample-store", "0")

@action_store.kubiya_action(validate_input=True)
def simple_action(a: str):
    "returns bar"
    return f"hi {a} from simple_action"
```

### We encourage you to use pydantic models for type annotation. Doing so will stregthen input validation. It will also enhance the functionality of Kubiyas no-code interface.

Successful response status code and JSON response body
```python
lass ExampleModel(BaseModel):
    """used for type hints, automatic decumentation and validation"""
    your_string: str
    your_int: int

@action_store.kubiya_action(validate_input=True)
def action_with_model(user: ExampleModel) -> str:
    """returns baz"""
    return f"{user.get('your_string')} | {user.get('your_int')} | {user.get('email')} from baz"
```
