from fastapi import FastAPI
import scraping
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello():
    return scraping.get_data()
