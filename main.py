
from fastapi import FastAPI, HTTPException, Request, Body, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError, validator, Field
from typing import Optional
import json

import datetime #Para las rutas '/index' y '/' quitar despues

#app = FastAPI(docs_url=None, redoc_url=None) #Para quitar las rutas /docs en productivo
app = FastAPI()

class Message(BaseModel):
    tag: Optional[str] = Field(max_length=100)

@app.post("/messages")
def messages(message: Message):
    return {"Mensaje": "Hola yo soy un chatbot. El tiempo es: " + str(datetime.datetime.now()), "tag": message.tag}

@app.get("/")
def index():

    return {"Mensaje": "Hola yo soy un chatbot. El tiempo es: " + str(datetime.datetime.now())}

