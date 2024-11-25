from fastapi import FastAPI
from routers.notes import NotesRouter
from routers.user import UserRouter

app = FastAPI(
    title="Notes Application API",
    description="A simple API for managing users and notes",
    version="1.0.0",
)


user_router = UserRouter() 
notes_router = NotesRouter()  


app.include_router(user_router.router, prefix="/user", tags=["Users"])
app.include_router(notes_router.router, prefix="/notes", tags=["Notes"])
