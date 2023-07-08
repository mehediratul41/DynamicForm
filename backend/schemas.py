from pydantic import BaseModel
from typing import List,Dict,Optional

# schemas for food information
# schemas for food information
# schemas for food information



#--------------------------------------------------New code Starts ------------------------------------------------------------


class FormEntryBase(BaseModel):
    form_id: int
    values: str 


class FormEntryCreate(FormEntryBase):
    pass


class FormEntry(FormEntryBase):
    # entry_id:int
    form_id: int
    values: str

    class Config:
        orm_mode = True

class FormEntryValues(BaseModel):
    values: str
    class Config:
        orm_mode = True




class FormStructureBase(BaseModel):
    form_id:int
    # form_name: str
    # keys: str
    # types: str



class FormStructureCreate(FormStructureBase):
    # form_id:int
    form_name: str
    keys: str
    types: str


class FormStructure(FormStructureBase):
    form_id=int
    form_name: str
    keys: str
    types: str
    # items: list[FormEntry] = []

    class Config:
        orm_mode = True


class FormStructureKeysTypes(BaseModel):
    keys: str
    types:str
    # items: list[FormEntry] = []

    class Config:
        orm_mode = True
        

class FormStructureKeysFormid(BaseModel):
    form_id:int
    keys: str
    # items: list[FormEntry] = []

    class Config:
        orm_mode = True        
        
        
        
class FormStructureFormName(BaseModel):
    form_name: str
    
    class Config:
        orm_mode = True
        
        
class FormStructureKey(BaseModel):
    keys: str
    
    class Config:
        orm_mode = True


#--------------------------------------------------New code Ends---------------------------------------------------------------

