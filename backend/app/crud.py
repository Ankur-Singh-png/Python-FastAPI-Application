from sqlalchemy.orm import Session
from app import models


def create_user(db: Session, username: str, password: str, email: str):
    new_user = models.User(
        username=username,
        email=email,
        password=password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(models.User)
            .filter(models.User.id == user_id)
            .first()
    )


def update_user(db: Session, user_id: int, uname: str):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:
        user.username = uname
        db.commit()
        db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:
        db.delete(user)
        db.commit()

    return user


# -----------------Folder Crud ---------------#

def create_folder(db: Session, name: str, owner_id: int):
    folder = models.Folder(
        name=name,
        owner_id=owner_id
    )

    db.add(folder)
    db.commit()
    db.refresh(folder)

    return folder


def get_all_folders(db: Session):
    return db.query(models.Folder).all()


def get_folder_by_id(db: Session, folder_id: int):
    return (
        db.query(models.Folder)
            .filter(models.Folder.id == folder_id)
            .first()
    )


def update_folder(db: Session, folder_id: int, name: str):
    folder = (
        db.query(models.Folder)
            .filter(models.Folder.id == folder_id)
            .first()
    )

    if folder:
        folder.name = name
        db.commit()
        db.refresh(folder)

    return folder


def delete_folder(db: Session, folder_id: int):
    folder = (
        db.query(models.Folder)
            .filter(models.Folder.id == folder_id)
            .first()
    )

    if folder:
        db.delete(folder)
        db.commit()

    return folder


# ------------ Document--------------- #


def create_document(db: Session, title: str, filename: str, folder_id: int, uploaded_id: int):
    document = models.Document(
        title=title,
        filename=filename,
        folder_id=folder_id,
        uploaded_by=uploaded_id
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def get_all_documents(db: Session):
    return db.query(models.Document).all()


def get_document_by_id(db: Session, document_id: int):
    return (
        db.query(models.Document)
        .filter(models.Document.id == document_id)
        .first()
    )


def update_document(db: Session, document_id: int, title: str):
    document = (
        db.query(models.Document)
        .filter(models.Document.id == document_id)
        .first()
    )
    if document:
        document.title = title,
        db.commit(),
        db.refresh(document)

    return document


def delete_document(db: Session, document_id: int):
    document = (
        db.query(models.Document)
            .filter(models.Document.id == document_id)
            .first()
    )
    if document:
        db.delete(document),
        db.refresh(document)
    return document
