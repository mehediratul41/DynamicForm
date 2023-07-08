from sqlalchemy.orm import Session
from . import models, schemas

# from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import text,MetaData, Table, Column,String, Integer, Date, create_engine
from typing import List
from .database import SessionLocal,engine
# from . import models, schemas
# from .schemas import ColumnNamesResponse,RowData, TableData,FormData
# from .models import ColumnNamesResponse,FormTable
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


