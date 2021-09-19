from fastapi import FastAPI, Request
from typing import List
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from . import models, schemas
from .Conexion import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

import json
from fastapi.encoders import jsonable_encoder


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory='./templates')

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/', response_model=List[schemas.Lenguaje])
def lenguajes(request:Request, db:Session=Depends(get_db)):
    languages = db.query(models.Lenguaje).all()
    result = jsonable_encoder(languages)
    return templates.TemplateResponse('index.html', {'request': request, 'lista': result})

@app.post('/add', response_model=schemas.Lenguaje)
async def add_language(request:Request, db:Session=Depends(get_db)):
    form_data = await request.form()
    language_form = form_data['lenguaje']
    languages = models.Lenguaje(nombre = language_form, id = 0)
    db.add(languages)
    db.commit()
    return RedirectResponse('/', 303)

@app.get('/eliminar/{lenguaje_id}', response_model=schemas.Respuesta)
def delete_languages(request:Request, lenguaje_id:int, db:Session=Depends(get_db)):
    language = db.query(models.Lenguaje).filter_by(id=lenguaje_id).first()
    print(language)
    db.delete(language)
    db.commit()
    respuesta = schemas.Respuesta(mensaje='Lenguaje eliminado exitosamente')
    return RedirectResponse('/', 303)