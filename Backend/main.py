from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine, Base
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer API"
    }