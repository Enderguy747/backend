from typing import Union
from fastapi import FastAPI
app = FastAPI()

#import routes here
from src.routes import routesDivDefNewton

#use routes here
#app.include_router(index.router)
app.include_router(routesDivDefNewton.router)


#default home api
@app.get("/")
def read_root():
    return {"Hello": "World"}


