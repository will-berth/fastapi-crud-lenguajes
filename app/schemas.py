from pydantic import BaseModel

class Lenguaje(BaseModel):
    id:int
    nombre:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str