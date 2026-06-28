from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None