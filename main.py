import logging

from fastapi import FastAPI
from fastapi_utils.timing import add_timing_middleware, record_timing
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from mathematics import fibonacci, factorial, ackermann, InvalidNumber

logging.basicConfig(level=logging.INFO, filename='logging.log')
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")
static_files_app = StaticFiles(directory=".")


@app.get('/fibonacci')
def fib(n: int, request: Request):
    return request_handler(request, fibonacci, n)


@app.get('/factorial')
def fact(n: int, request: Request):
    return request_handler(request, factorial, n)


@app.get('/ackermann')
def ack(m: int, n: int, request: Request):
    return request_handler(request, ackermann, m, n)


def request_handler(request, func, *args):
    try:
        record_timing(request, note="before")
        msg = {'result': str(func(*args))}
        record_timing(request, note="after")
    except InvalidNumber:
        msg = {'message': 'Invalid number'}

    return msg
