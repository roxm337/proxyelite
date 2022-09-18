# main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

machine_ip = requests.get('http://ipecho.net/plain?').text

@app.get("/",response_class=PlainTextResponse)
def hello():
    return f'ip: {machine_ip}'

