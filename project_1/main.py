from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 for templates
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://dp55954:password@cluster0.rcbvl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# ✅ Corrected Route for Home Page
@app.get("/",response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.test.test.find()
    for doc in docs:
        print(doc)
    print(docs)
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
