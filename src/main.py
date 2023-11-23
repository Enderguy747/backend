from typing import Union
from fastapi import FastAPI
app = FastAPI()

#import routes here
from src.routes import index

#use routes here
app.include_router(index.router)


#default home api
@app.get("/")
def read_root():
    return {"Hello": "World"}


