from sqlalchemy.orm import Session
from . import models, schemas

# from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import text,MetaData, Table, Column,String, Integer, Date, create_engine
from typing import List
from .database import SessionLocal,engine
# from . import models, schemas
# from .schemas import ColumnNamesResponse,RowData, TableData,FormData
from .models import ColumnNamesResponse,FormTable
from typing import List,Dict
from fastapi import APIRouter
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
metadata = MetaData()
router = APIRouter()

#--------------------------------------------------New code Starts ------------------------------------------------------------


def get_formstructure(db: Session, id: int):
    return db.query(models.FormStructure).filter(models.FormStructure.form_id == id).first()


def get_formstructure_by_form_name(db: Session, form_name: str):
    return db.query(models.FormStructure).filter(models.FormStructure.form_name == form_name).first()


def get_formstructure_keys_and_types_by_form_name(db: Session, form_name: str):
    return db.query(models.FormStructure).filter(models.FormStructure.form_name == form_name).first()

def get_formstructure_formname(db: Session):
    return db.query(models.FormStructure).all()



def get_formstructure(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FormStructure).offset(skip).limit(limit).all()


def create_formstructure(db: Session, formstructure: schemas.FormStructureCreate):
    db_formstructure = models.FormStructure(**formstructure.dict())
    db.add(db_formstructure)
    db.commit()
    db.refresh(db_formstructure)
    return db_formstructure



def create_formentry(db: Session, formentry: schemas.FormEntryCreate):
    db_formentry = models.FormEntry(**formentry.dict())
    db.add(db_formentry)
    db.commit()
    db.refresh(db_formentry)
    return db_formentry



def get_formentry(db: Session):
    return db.query(models.FormEntry).all()


def get_formentryvalues(db: Session,form_id:int):
    return db.query(models.FormEntry).filter(models.FormEntry.form_id == form_id).all()

#--------------------------------------------------New code Ends---------------------------------------------------------------





# # Example route and endpoint handler
# @router.get("/items")
# def get_items():
#     # Your logic to fetch items from the database or any other source
#     items = ["item1", "item2", "item3"]
#     return {"items": items}

# @router.post("/items")
# def create_item(item: str):
#     # Your logic to create a new item in the database or any other action
#     return {"message": f"Item '{item}' created successfully"}


# # def get_user(db: Session, user_id: int):
# #     return db.query(models.User).filter(models.User.id == user_id).first()


# # def get_user_by_email(db: Session, email: str):
# #     return db.query(models.User).filter(models.User.email == email).first()


# # def get_users(db: Session, skip: int = 0, limit: int = 100):
# #     return db.query(models.User).offset(skip).limit(limit).all()


# # def create_user(db: Session, user: schemas.UserCreate):
# #     fake_hashed_password = user.password + "notreallyhashed"
# #     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
# #     db.add(db_user)
# #     db.commit()
# #     db.refresh(db_user)
# #     return db_user


# #request for food table

# def get_foods(db: Session, skip: int = 0, limit: int = 100,id=id):
#     return db.query(models.FoodInformation).offset(skip).limit(limit).all()


# def create_food(db: Session, item: schemas.FoodCreate):
#     db_food = models.FoodInformation(**item.dict())
#     db.add(db_food)
#     db.commit()
#     db.refresh(db_food)
#     return db_food

# #-----------------------------------------request for vehicle table--------------------------------------------


# def get_vehicle(db: Session, skip: int = 0, limit: int = 100,id=id):
#     return db.query(models.VehicleInformation).offset(skip).limit(limit).all()


# def create_vehicle(db: Session, item: schemas.VehicleCreate):
#     db_vehicle = models.VehicleInformation(**item.dict())
#     db.add(db_vehicle)
#     db.commit()
#     db.refresh(db_vehicle)
#     return db_vehicle

# #------------------------------------------request for vehicle table end-------------------------------------------

# # --------------------------------------------------------Get column names-----------------------------------


# def get_column_names(db, table_name):
#     query = text(f"PRAGMA table_info('{table_name}')")
#     result = db.execute(query)
#     column_names = [row[1] for row in result]
#     return column_names


# #------------------------------------------------------Get column names--------------------------------------------------

# #----------------------------------------------------make row --------------------------------------------
# async def create_row(table_name: str, row_data: RowData) -> TableData:
#     db = Database()
#     await db.connect()
#     result = await db.insert_row(table_name, row_data)
#     await db.disconnect()
#     return result
# #----------------------------------------------------make row end-------------------------------------------


# #--------------------------------------------------New table-------------------------------------------





# class FormData(Base):
#     __tablename__ = 'form_data'

#     id = Column(Integer, primary_key=True, index=True)
#     form_name = Column(String, index=True)


# def create_form_table(table_name, form_fields):
#     columns = []
#     for field in form_fields:
#         column_name = field.field_name.lower().replace(" ", "_")
#         value_type = field.value_type.lower()

#         if value_type == 'text' or value_type == 'string':
#             column = Column(String, index=True)
#         elif value_type == 'number' or value_type == 'integer':
#             column = Column(Integer, index=True)
#         elif value_type == 'date':
#             column = Column(Date, index=True)
#         else:
#             column = Column(String, index=True)

#         column_name = get_unique_column_name(columns, column_name)
#         columns.append((column_name, column))

#     metadata = Base.metadata
#     for column_name, column in columns:
#         column_name = get_unique_column_name(columns, column_name)
#         column._set_parent(metadata, column_name)
#     metadata.create_all(bind=get_engine())


# def get_engine():
#     global engine
#     if engine is None:
#         SQLALCHEMY_DATABASE_URL = 'sqlite:///form.db'
#         engine = create_engine(SQLALCHEMY_DATABASE_URL)
#     return engine


# def get_unique_column_name(columns, column_name):
#     existing_columns = [column[0] for column in columns]
#     if column_name in existing_columns:
#         suffix = 1
#         while f"{column_name}_{suffix}" in existing_columns:
#             suffix += 1
#         column_name = f"{column_name}_{suffix}"
#     return column_name


# #--------------------------------------------------New Table end---------------------------------------



# #--------------------------------------------------New Code for Table ------------------------------

# def handle_form_submission(form_data):
#     form_name = form_data['formName']
#     fields = form_data['fields']

#     # Define dynamic table class
#     class DynamicForm(Base):
#         __tablename__ = form_name
#         id = Column(String, primary_key=True)

#     # Add dynamic columns to the dynamic table
#     for index, field in enumerate(fields):
#         column_name = field['columnName']
#         data_type = field['dataType']
#         setattr(DynamicForm, f"column_{index}", Column(data_type))

#     # Create table in the database
#     Base.metadata.create_all(bind=engine)

#     # Example: Insert data into the dynamic table
#     session = SessionLocal()
#     session.add(DynamicForm(id='example_id', column_0='example_value_0', column_1='example_value_1'))
#     session.commit()
#     session.close()

# #--------------------------------------------------New Code for Table------------------------------