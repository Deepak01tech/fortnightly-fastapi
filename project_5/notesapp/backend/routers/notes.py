from fastapi import FastAPI, Depends, status, Response

from backend.database import database

router = FastAPI()
