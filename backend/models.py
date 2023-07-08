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
