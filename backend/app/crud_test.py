from app.database import SessionLocal
from app import crud

db = SessionLocal

try:
    user = crud.create_user(
        db=db,
        username = "ankur",
        password="root",
        email= "ankursinghyoyo@gmail.com"
    )
    print("User created successfully!")
    print(f"ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
finally:
    db.close()