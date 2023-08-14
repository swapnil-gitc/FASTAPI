from fastapi import FastAPI
from routes.note import note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(note)
