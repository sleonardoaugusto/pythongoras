## How develop?

1. Create a virtualenv with Python 3.x.
2. Activate virtualenv.
3. Install dependencies.
4. Run tests.
5. Run server.

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn main:app --reload
```

## Resources
http://localhost:8000/fibonacci?n=42
http://localhost:8000/factorial?n=42
http://localhost:8000/ackermann?m=1&n=1

## Logging
All logging requests will be available in __logging.log__