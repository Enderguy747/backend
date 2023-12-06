from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import routesDivDefNewton,routesLaGrange,routesMinCuadrados

app = FastAPI()


#CORS
'''
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://:8080",
'''
origins = [
"http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#import routes here
#use routes here
#app.include_router(index.router)
app.include_router(routesDivDefNewton.router)
app.include_router(routesLaGrange.router)
app.include_router(routesMinCuadrados.router)


#default home api
@app.get("/")
def read_root():
    return {"API Rest Proyecto Metodos Numericos"}


