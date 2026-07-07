from fastapi import APIRouter, HTTPException

from app.database import SessionLocal
from app import crud

router = APIRouter(
    prefix="/folders",
    tags=["Folders"]
)


@router.post("/")
def create_folder(name: str, owner_id: int):
    db = SessionLocal()

    try:
        return crud.create_folder(db, name, owner_id)
    finally:
        db.close()


@router.get("/")
def get_all_folders():
    db = SessionLocal()

    try:
        return crud.get_all_folders(db)
    finally:
        db.close()


@router.get("/{folder_id}")
def get_folder(folder_id: int):
    db = SessionLocal()

    try:
        folder = crud.get_folder_by_id(db, folder_id)

        if folder is None:
            raise HTTPException(404, "Folder not found")

        return folder

    finally:
        db.close()


@router.put("/{folder_id}")
def update_folder(folder_id: int, name: str):
    db = SessionLocal()

    try:
        folder = crud.update_folder(db, folder_id, name)

        if folder is None:
            raise HTTPException(404, "Folder not found")

        return folder

    finally:
        db.close()


@router.delete("/{folder_id}")
def delete_folder(folder_id: int):
    db = SessionLocal()

    try:
        folder = crud.delete_folder(db, folder_id)

        if folder is None:
            raise HTTPException(404, "Folder not found")

        return {"message": "Folder deleted successfully"}

    finally:
        db.close()