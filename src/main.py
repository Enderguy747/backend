from fastapi import FastAPI
app = FastAPI()

#import routes here
from src.routes import routesDivDefNewton,routesLaGrange

#use routes here
#app.include_router(index.router)
app.include_router(routesDivDefNewton.router)
app.include_router(routesLaGrange.router)



#default home api
@app.get("/")
def read_root():
    return {"API Rest Proyecto Metodos Numericos"}


