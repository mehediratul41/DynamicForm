
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
from .models import create_dynamic_table
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









# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
# #     return db_user
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/food/", response_model=schemas.Food)
# def create_food(
#      item: schemas.FoodCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_food(db=db, item=item)


# @app.get("/food/", response_model=list[schemas.Food])
# def read_food(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     foods = crud.get_foods(db, skip=skip, limit=limit,id=id)
#     return foods

# #------------------------------Request for vehicle------------------------------

# @app.post("/vehicle/", response_model=schemas.Vehicle)
# def create_vehicle(
#      item: schemas.VehicleCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_vehicle(db=db, item=item)


# @app.get("/vehicle/", response_model=list[schemas.Vehicle])
# def read_vehicle(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     vehicle = crud.get_vehicle(db, skip=skip, limit=limit,id=id)
#     return vehicle




# #------------------------------------dynamic table name ---------------------------------------

# @app.get("/table_names")
# def get_table_names():
#     # Create an SQLAlchemy inspector
#     insp = Inspector.from_engine(engine)

#     # Retrieve the table names from the database
#     table_names = insp.get_table_names()

#     return {"table_names": table_names}


# #-----------------------------------dynamic table name End----------------------------------------------

# #-----------------------------------dynamic table Get column Name--------------------------------------------
# @app.get("/column_names/{table_name}", response_model=schemas.ColumnNamesResponse)
# def read_column_names(table_name: str, db: Session = Depends(get_db)):
#     column_names = crud.get_column_names(db, table_name)
#     return schemas.ColumnNamesResponse(column_names=column_names)
# #-----------------------------------dynamic table Get column Name--------------------------------------------


# #----------------------------------------------------dynamic create table ---------------------------

# @app.post('/create-form')
# def create_form(form_data: FormData, db=Depends(get_db)):
#     try:
#         create_form_table(form_data)
#         return {'message': 'Table created successfully'}
#     except Exception as e:
#         return {'message': 'Error creating table', 'error': str(e)}
# #---------------------------------------------------dynamic create table  end------------------------------

# #----------------------------------------------------New code for Table creation-------------------------------------------

# @app.post('/submit-form')
# def submit_form(form_data: dict):
#     handle_form_submission(form_data)
#     return {'message': 'Form submitted successfully'}

# #----------------------------------------------------- New code for Table creation End--------------------------------------


# #--------------------------------------------Dynamically Typed form-----------------------------------
# @app.post("/create_table")
# def create_table(request_data: dict):
#     table_name = request_data.get("table_name")
#     columns = request_data.get("columns")

#     if not table_name or not columns:
#         return {"message": "Invalid request"}

#     create_dynamic_table(table_name, columns)
#     return {"message": "Table created successfully"}
# #--------------------------------------------Dynamically Typed form-----------------------------------