from fastapi import FastAPI
from app.routes import users, documents, folders
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Knowledge Vault API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(folders.router)
app.include_router(documents.router)


@app.get("/")
def home():
    return {
        "message": "Knowledge Vault API is running"
    }
