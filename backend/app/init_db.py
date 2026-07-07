from app.database import Base,engine
from app import models

print("Creating Database Tables")

Base.metadata.create_all(bind=engine)

print("Database Running Sucessfully")