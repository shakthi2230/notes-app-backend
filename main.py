from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.notes import NotesRouter
from routers.user import UserRouter

app = FastAPI(
    title="Notes Application API",
    description="A simple API for managing users and notes",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

user_router = UserRouter() 
notes_router = NotesRouter()  

@app.get("/")
async def root():
    return {"message": "Welcome to the API Notes App!"}

app.include_router(user_router.router, prefix="/user", tags=["Users"])
app.include_router(notes_router.router, prefix="/notes", tags=["Notes"])
