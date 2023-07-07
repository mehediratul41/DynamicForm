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


# class FoodInformation(BaseModel):
#     name: str
#     calories: int 
#     category: str
#     plantScientificName: str
#     origin: str   
    


# class FoodCreate(FoodInformation):
#     pass


# class Food(FoodInformation):
    
#     name: str
#     calories: int 
#     category: str
#     plantScientificName: str
#     origin: str  

#     class Config:
#         orm_mode = True


# # schemas for food information
# # schemas for food information       
# # schemas for food information


# class VehicleInformation(BaseModel):
#     type: str
#     year: int 
#     milage: int
    


# class VehicleCreate(VehicleInformation):
#     pass


# class Vehicle(VehicleInformation):
#     id: int
#     type: str
#     year: int 
#     milage: int

#     class Config:
#         orm_mode = True
        
# #------------------------------get table names---------------------------------    
# class ColumnNamesResponse(BaseModel):
#     column_names: List[str]
    
# #------------------------------get table names end-----------------------------

# #----------------------------------------Create a new row-----------------------------

# class RowData(BaseModel):
#     column_names: List[str]
#     values: List[str]

# class TableData(BaseModel):
#     table_name: str
#     column_names: List[str]
#     values: List[List[str]]
# #----------------------------------------Create a new row-----------------------------


# #-------------------------------Get   column names---------------------------------
# class ColumnNamesResponse(BaseModel):
#     column_names: List[str]
# #--------------------------------Get  column names--------------------------------

# #-----------------------------------Insert new row in the table----------------------------------------

# class DynamicTableItem(BaseModel):
#     columns: Dict[str, str]

# #-----------------------------------Insert new row in the table ---------------------------------------



# #--------------------------------------------------Table creation on database---------------------------------------------
# class FormField(BaseModel):
#     fieldName: str
#     valueType: str


# class FormData(BaseModel):
#     formName: str
#     formFields: List[FormField]
# #--------------------------------------------------Table creation on database --------------------------------------------



# #-----------------------------------------------------------New code for table-------------------------------------------
# class Field(BaseModel):
#     columnName: str
#     dataType: str

# class DynamicFormData(BaseModel):
#     formName: str
#     fields: list[Field]
# #------------------------------------------------------------New code for table ----------------------------------------