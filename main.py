import validators
from fastapi import FastAPI, HTTPException

from . import schemas

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World!"}

@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request("Invalid URL")
    return {"targetUrl": url.target_url}