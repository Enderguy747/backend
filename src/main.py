from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


#CORS

origins = [
'''
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://:8080",
'''
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
from src.routes import routesDivDefNewton,routesLaGrange

#use routes here
#app.include_router(index.router)
app.include_router(routesDivDefNewton.router)
app.include_router(routesLaGrange.router)



#default home api
@app.get("/")
def read_root():
    return {"API Rest Proyecto Metodos Numericos"}


