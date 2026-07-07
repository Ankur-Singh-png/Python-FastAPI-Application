from fastapi import APIRouter, HTTPException

from app import crud
from app.database import SessionLocal

router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)


@router.get("/")
def get_users():
    db = SessionLocal()

    try:
        users= crud.get_all_user(db)
        return users
    finally:
        db.close()


@router.post("/")
def create_user(username: str, email: str, password: str):
    db = SessionLocal()

    try:
        user = crud.create_user(
            db= db,
            username=username,
            password=password,
            email=email
        )
        return user
    finally:
        db.close()


@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    db = SessionLocal()

    try:
        user = crud.get_user_by_id(db,user_id)

        if user is None:
            raise HTTPException(
                status_code="404",
                detail="Not Found"
            )
        return user
    finally:
        db.close()


@router.put("/{user_id}")
def update_user(user_id: int, username: str):
    db = SessionLocal()
    try:
        user = crud.update_user(
            db=db,
            uname=username,
            user_id=user_id
        )
        if user is None:
            raise HTTPException(
                status_code="404",
                detail="User not Found"
            )
        return user
    finally:
        db.close()


@router.delete("/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()

    try:
        user = crud.delete_user(
            db=db,
            user_id=user_id
        )
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="user not found"
            )
        return {
           "message": "User Deleted Successfully"
        }

    finally:
        db.close()


