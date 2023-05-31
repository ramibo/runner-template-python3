from function import main_store
import os
import sys
import signal
import time

def run() -> None:  # pragma: no cover
    """Run the server."""
    import uvicorn

    uvicorn.run(
        "server.api:app", host="127.0.0.1", port=8000, reload=False
    )
    
def SignalHandler(SignalNumber, Frame):
    timeout = os.getenv("write_timeout")
    sys.stderr.write('Function got SIGTERM, draining for up to: {}\n'.format(timeout))
    sys.stderr.flush()

if __name__ == "__main__":
    run()
    signal.signal(signal.SIGTERM, SignalHandler)
