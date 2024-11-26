from fastapi import APIRouter, HTTPException, Depends
from models.notes import NotesModel
from schema.notes import NoteCreateRequest, NoteUpdateRequest
from authentication.authentication import Authentication
from fastapi.security import OAuth2PasswordBearer


class NotesRouter:
    def __init__(self):
        self.router = APIRouter()
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
        self.register_routes()

    def register_routes(self):
        self.router.post("/")(self.create_note)
        self.router.get("/")(self.get_notes)
        self.router.put("/")(self.edit_note)
        self.router.delete("/{note_id}")(self.delete_note)

    def create_note(
        self, note_data: NoteCreateRequest, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))
    ):
        """
        Endpoint to create a new note for the authenticated user.
        """
        current_user = Authentication.get_current_user(token)
        note_id = NotesModel.create_note(current_user["user_id"], note_data.note_title, note_data.note_content)
        return {"note_id": note_id, "message": "Note created successfully"}

    def get_notes(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))):
        """
        Endpoint to retrieve all notes for the authenticated user.
        """
        current_user = Authentication.get_current_user(token)
        notes = NotesModel.get_notes_by_user(current_user["user_id"])
        # if not notes:
        #     raise HTTPException(status_code=404, detail="No notes found")
        return {"notes": notes}

    def edit_note(
        self, note_data: NoteUpdateRequest, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))
    ):
        """
        Endpoint to edit a note for the authenticated user.
        """
        current_user = Authentication.get_current_user(token)
        NotesModel.update_note(note_data.note_id, note_data.note_title, note_data.note_content)
        return {"message": "Note updated successfully"}

    def delete_note(self, note_id: str, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))):
        """
        Endpoint to delete a note for the authenticated user.
        """
        current_user = Authentication.get_current_user(token)
        user_id = current_user["user_id"]

        notes = NotesModel.get_notes_by_user(user_id)
        if not notes:
            raise HTTPException(status_code=404, detail="No notes found for this user")

        note_to_delete = next((note for note in notes if note["note_id"] == note_id), None)
        if not note_to_delete:
            raise HTTPException(status_code=404, detail="Note with the given ID not found")

        NotesModel.delete_note(note_id)
        return {"message": "Note deleted successfully"}



notes_router = NotesRouter().router
