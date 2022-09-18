# main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/",response_class=PlainTextResponse)
def hello():
    return 
'''
120.194.55.139:5678
190.0.22.35:61155
180.92.226.137:8291
95.38.75.238:4145
182.253.86.202:4145
125.125.26.84:7890
124.113.216.42:57114
27.157.228.39:53309
183.184.111.21:1080
24.249.199.12:4145
117.212.24.237:5678
78.31.73.101:8291
192.252.211.197:14921
'''
