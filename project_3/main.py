from fastapi import FastAPI
from routes import blog  # Import routes

app = FastAPI()


app.include_router(blog.router)


@app.get("/")
def home():
    return {"message": "Welcome to Project 3 API"}

