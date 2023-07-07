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












# #-----------------------------Get column Names---------------------------------

# def get_table_column_names(table_name: str) -> List[str]:
#     conn = sqlite3.connect("form.db")  # Replace with your database connection
#     cursor = conn.cursor()
#     cursor.execute(f"PRAGMA table_info({table_name})")
#     column_info = cursor.fetchall()
#     column_names = [col[1] for col in column_info]
#     cursor.close()
#     conn.close()
#     return column_names
# #--------------------------------Get Column--------------------------------------------------

# #--------------------------------------Dependencies for create table------------------------------------
# def get_db() -> Session:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def get_table_column_names(table):
#     return table.__table__.columns.keys()
# #---------------------------------------Dependencies for create table----------------------------------


# #-------------------------------------------Create row in the table-------------------------------

# class Database:
#     def __init__(self):
#         self.conn = None

#     async def connect(self):
#         self.conn = sqlite3.connect("form.db")

#     async def disconnect(self):
#         if self.conn:
#             self.conn.close()

#     async def insert_row(self, table_name: str, row_data: RowData) -> TableData:
#         cursor = self.conn.cursor()

#         # Build the SQL query
#         columns = ', '.join(row_data.column_names)
#         values = ', '.join(['?' for _ in row_data.column_names])
#         query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

#         try:
#             # Execute the query with the provided values
#             cursor.execute(query, row_data.values)
#             self.conn.commit()

#             # Retrieve the inserted row
#             cursor.execute(f"SELECT * FROM {table_name} WHERE rowid=?", (cursor.lastrowid,))
#             inserted_row = cursor.fetchone()

#             # Prepare the response
#             table_data = TableData(
#                 table_name=table_name,
#                 column_names=row_data.column_names,
#                 values=[inserted_row]
#             )
#             return table_data

#         except sqlite3.Error as e:
#             raise Exception(f"Failed to insert row: {str(e)}")

# #--------------------------------------------Create row in the table-------------------------------
