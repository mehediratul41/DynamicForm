from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#---------------------------------------------New Import files---------------------------------------------------------------

#----------------------------------------------New Database Connection------------------------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./form.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#-----------------------------------------------New Database Connection------------------------------------------------------

from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import sqlite3
from typing import List

# from .schemas import RowData, TableData


# Create the metadata object
metadata = MetaData()

# Bind the metadata object to the engine
metadata.bind = engine

#--------------------------------------------------New code Starts ------------------------------------------------------------


#--------------------------------------------------New code Ends---------------------------------------------------------------

