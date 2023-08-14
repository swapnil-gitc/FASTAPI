from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import NoteEntity, NotesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #docs = conn.notes.notes.find_one({})
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            # "note": doc["note"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]


        })
        # print(doc)
    # print(newDocs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    # print(form)
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success": True}
