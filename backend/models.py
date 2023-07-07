from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table,Date
from sqlalchemy.orm import relationship
from .database import Base

#--------------------------------------------------New Imports Inheritances--------------------------------------------------


from typing import List
from .database import  engine, SessionLocal, Base,metadata
from sqlalchemy import create_engine, MetaData
# from .database import Database


#--------------------------------------------------New code Starts ------------------------------------------------------------


class FormStructure(Base):
    __tablename__ = "FormStructure"

    form_id = Column(Integer, primary_key=True, index=True)
    form_name = Column(String, unique=True, index=True)
    keys = Column(String,index=True)
    types = Column(String,  index=True)


    formentrys = relationship("FormEntry", back_populates="formstructure")


class FormEntry(Base):
    __tablename__ = "FormEntry"

    entry_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("FormStructure.form_id"))
    values = Column(String, index=True)


    formstructure = relationship("FormStructure", back_populates="formentrys")


#--------------------------------------------------New code Ends---------------------------------------------------------------



#-----------------------------------------------------------------Old code here----------------------------------------------------

#FoodInformation

class FoodInformation(Base):
    __tablename__ = "Food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    calories = Column(Integer, index=True)
    category = Column(String, index=True)
    plantScientificName = Column(String, index = True)
    origin = Column(String, index = True)


#VehicleInformation


class VehicleInformation(Base):
    __tablename__ = "Vehicle"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    year = Column(Integer, index=True)
    milage = Column(Integer, index=True)

# -------------------------------------------------Get column name----------------------------------


class ColumnNamesResponse(Base):
    __tablename__ = "column_names_response"

    id = Column(Integer, primary_key=True, index=True)
    column_names = Column(String)
# class ColumnNamesResponse(Base):
#     __tablename__ = "column_names_response"

#     id = Column(Integer, primary_key=True, index=True)
#     column_names = Column(String)
#----------------------------------------------------Get Column Name-------------------------------


#------------------------------------------------Create New table ---------------------------------
class FormTable(Base):
    __tablename__ = 'form_tables'

    id = Column(Integer, primary_key=True, index=True)
    form_name = Column(String, unique=True, index=True)

#-----------------------------------------------Create New table ----------------------------------

#------------------------------------New code for form creation-----------------------------------

# def create_table(table_name, columns):
#     class DynamicFormData(Base):
#         __tablename__ = table_name
#         id = Column(Integer, primary_key=True, index=True)
#         # Dynamically create columns based on form submission
#         for column in columns:
#             setattr(DynamicFormData, column['columnName'], Column(String))

#     return DynamicFormData

# Base.metadata.create_all(bind=engine)

#-------------------------------------New code for form creation End------------------------------

#-------------------------------------Dynamically typed form--------------------------------------

def create_dynamic_table(table_name, columns):
    # Define the table dynamically
    table = Table(
        table_name,
        metadata,
        *(Column(column_name, String() if data_type == 'text' else Integer()) for column_name, data_type in columns)
    )
    
    # Create the table in the database
    metadata.create_all(tables=[table])

#--------------------------------------Dynamically typed form-------------------------------------