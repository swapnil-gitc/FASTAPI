#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb://localhost:27017")
# @app.get("/")
# def read_root():
#    return {"Hello": "World"}


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #docs = conn.notes.notes.find_one({})
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
        print(doc)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
