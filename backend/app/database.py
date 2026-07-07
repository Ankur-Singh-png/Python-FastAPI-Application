# This file contains description and connection with the database
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# to load environment variables
load_dotenv()

database_url = os.getenv("DATABASE_URL")

# Create Database Engine
engine = create_engine(database_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    # Tells to use this session whenever we interact with database
    bind=engine
)

# Base class for all modules
Base = declarative_base()

