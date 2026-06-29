from fastapi import APIRouter, Depends
from app.schemas.todoschemas import TodoCreate, TodoResponse, TodoUpdate
from app.core.db import getsession
from sqlalchemy.orm import Session
from app.core.security import token_verify
from app.services.task_services import TaskService
from app.models.models import User

todorouter = APIRouter(prefix="/todo", tags=["todos"])

@todorouter.post("/create", response_model=TodoResponse)
async def create_task(body: TodoCreate, session: Session = Depends(getsession), user: User = Depends(token_verify)):
    n_task = TaskService(session)
    new_task = n_task.create_task(body.title, user.id)
    return new_task

@todorouter.get("/", response_model=list[TodoResponse])
async def show_tasks(session: Session = Depends(getsession), user: User = Depends(token_verify)):
    list = TaskService(session)
    task_list = list.list_tasks(user.id)
    return task_list

@todorouter.put("/update/{task_id}", response_model=TodoResponse)
async def update_task(task_id: int, body: TodoUpdate ,user: User = Depends(token_verify), session: Session = Depends(getsession)):
    update = TaskService(session)
    updated_task = update.update_task(task_id, user.id, body.title, body.done)
    return updated_task

@todorouter.delete("/delete/{task_id}")
async def delete_task(task_id: int, user: User = Depends(token_verify), session: Session = Depends(getsession)):
    delete = TaskService(session)  
    deleted_task = delete.delete_tasks(task_id, user.id)
    return deleted_task