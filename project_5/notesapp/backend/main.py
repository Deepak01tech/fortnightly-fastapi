from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from backend.database.database import engine,Base
from pymongo import MongoClient
from backend import router  # Import the router from the backend package



app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

conn = MongoClient("mongodb+srv://dp55954:HXuZXdRAqBU193Os@cluster0.rcbvl.mongodb.net/notesapp?retryWrites=true&w=majority")
db = conn["notesapp"]
collection = db["notes"]

app.include_router(router)  # Include the router
  # Include the router

@app.get("/",response_class=HtmlResponse)
async def index(request: Request):
    docs = conn.notesapp.notes.find({})
    for doc in docs:
        print(doc["_id"])
    return templates.TemplateResponse("index.html", {"request": request})




