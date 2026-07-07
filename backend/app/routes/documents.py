from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app import crud

router = APIRouter(
    prefix= "/documents",
    tags=["Documents"]
)


@router.post("/")
def create_document(title: str, filename: str, folder_id: int, uploaded_id: int):
    db= SessionLocal()
    try:
        return crud.create_document(db, title, filename, folder_id, uploaded_id)
    finally:
        db.close()


@router.get("/")
def get_all_documents():
    db = SessionLocal()
    try:
        return crud.get_all_documents(db)
    finally:
        db.close()


@router.get("/{document_id}")
def get_document_by_id(document_id: int):
    db = SessionLocal()
    try:
        document = crud.get_document_by_id(db,document_id)

        if document is None:
            raise HTTPException(
                status_code=404,
                detail= "Document Not Found"
            )
        return document
    finally:
        db.close()


@router.put("/{document_id}")
def update_document(document_id: int, title: str):
    db = SessionLocal()

    try:
        document = crud.update_document(db, document_id, title )

        if document is None:
            raise HTTPException(
                status_code= 404,
                detail= "Document not found"
            )
        return document
    finally:
        db.close()


@router.delete("/{document_id}")
def delete_document(document_id: int):
    db= SessionLocal()

    try:
        document = crud.delete_document(db,document_id)

        if document is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )
        return "Document deleted successfully"
    finally:
        db.close()