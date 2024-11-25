
from pydantic import BaseModel

class NoteCreateRequest(BaseModel):
    note_title: str
    note_content: str


class NoteUpdateRequest(BaseModel):
    note_id: str
    note_title: str
    note_content: str
