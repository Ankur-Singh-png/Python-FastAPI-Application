from sqlalchemy import Integer, ForeignKey, String,Column
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username= Column(String(100),nullable=False)
    email = Column(String(255),nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(100),default='User')


class Folder(Base):
    __tablename__ = "folders"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    title = Column(String(255),nullable=False)
    filename = Column(String(255),nullable=False)
    folder_id = Column(
        Integer,
        ForeignKey("folders.id")
    )
    uploaded_by = Column(
        Integer,
        ForeignKey("users.id")
    )




