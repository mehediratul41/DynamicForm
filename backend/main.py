
from fastapi import Depends, FastAPI, HTTPException,APIRouter, Request, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
#-----------------------------------------------------New Imports--------------------------------------------------------


from fastapi.params import Depends
from fastapi.responses import JSONResponse
# from sqlalchemy.orm import Session
# from . import  crud,models,schemas
# from .database import Database

# from .crud import get_column_names, create_form_table
# from .models import create_dynamic_table
# from .schemas import ColumnNamesResponse,TableData, RowData,FormData
from .crud import router as crud_router
# from .database import SessionLocal, engine
# from .crud import create_row,handle_form_submission
from typing import List,Dict
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.engine.reflection import Inspector



#-----------------------------------------------------Database Creation--------------------------------------------------------

models.Base.metadata.create_all(bind=engine)

#----------------------------------------------------Database Creation End---------------------------------------------------------

app = FastAPI()

# database = Database()  # Instantiate the Database class


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


#-----------------------------------------------------Crosorigin Resource Sharing--------------------------------------------

origins = [
    "http://localhost:5173"
]

#adding CrosOrigin Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------Dependency-------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#---------------------------------------------------------New code-------------------------------------------------------------

@app.post("/formstructure", response_model=schemas.FormStructure ,tags=["New API's"])
def create_formstructure(formstructure: schemas.FormStructureCreate, db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_by_form_name(db, form_name=formstructure.form_name)
    if db_formstructure:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_formstructure(db=db, formstructure=formstructure)


@app.get("/formstructure/", response_model=list[schemas.FormStructure],tags=["New API's"])
def read_formstructure(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    formstructure = crud.get_formstructure(db, skip=skip, limit=limit)
    return formstructure


@app.get("/formstructure/{form_name}}", response_model=schemas.FormStructure ,tags=["New API's"])
def read_formstructure(form_name: str, db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_by_form_name(db, form_name=form_name)
    if db_formstructure is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_formstructure
#------------------------------FormKey and Types-------------------------------
@app.get("/formstructurekeyandtypes/{form_name}", response_model=schemas.FormStructureKeysTypes ,tags=["New API's"])
def read_formstructure(form_name: str, db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_keys_and_types_by_form_name(db, form_name=form_name)
    if db_formstructure is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_formstructure

#--------------------------------Form Keys and Types End--------------------------------
#----------------------------------------Get form keys-----------------------------------
@app.get("/formstructurekey/{form_name}", response_model=schemas.FormStructureKey ,tags=["New API's"])
def read_formstructure(form_name: str, db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_keys_and_types_by_form_name(db, form_name=form_name)
    if db_formstructure is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_formstructure

#-----------------------------------------Get form keys end------------------------------



#-------------------------------------Form Id---------------------------------------
@app.get("/formstructurekeyandformid/{form_name}", response_model=schemas.FormStructureKeysFormid ,tags=["New API's"])
def read_formstructure(form_name: str, db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_keys_and_types_by_form_name(db, form_name=form_name)
    if db_formstructure is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_formstructure

#--------------------------------------Form Id end----------------------------------
#------------------------------Form Names ---------------------------------------
@app.get("/formstructureformnames", response_model=list[schemas.FormStructureFormName] ,tags=["New API's"])
def read_formstructure( db: Session = Depends(get_db)):
    db_formstructure = crud.get_formstructure_formname(db)
    if db_formstructure is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_formstructure

#-------------------------------Form Names End-----------------------------------

@app.post("/formentry", response_model=schemas.FormEntry ,tags=["New API's"])
def create_formentry_for_formstructure(
   formentry: schemas.FormEntryCreate, db: Session = Depends(get_db)
):
    return crud.create_formentry(db=db, formentry=formentry)


@app.get("/formentry/", response_model=list[schemas.FormEntry] ,tags=["New API's"])
def read_formentry( db: Session = Depends(get_db)):
    read_formentry = crud.get_formentry(db)
    return read_formentry


#----------------------------------------------Get from entry values based on Form_id-----------------------------


@app.get("/formentry/{form_id}", response_model=list[schemas.FormEntryValues] ,tags=["New API's"])
def read_formentry(form_id:int, db: Session = Depends(get_db)):
    read_formentry = crud.get_formentryvalues(db, form_id=form_id)
    return read_formentry


#----------------------------------------------Get from entry values based on Form_id-----------------------------

#---------------------------------------------------------New Code End---------------------------------------------------------

