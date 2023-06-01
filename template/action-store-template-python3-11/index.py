from function import main_store


def run() -> None:  # pragma: no cover
    """Run the server."""
    import uvicorn

    uvicorn.run("server.api:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    run()
