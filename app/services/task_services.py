from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import Tasks

class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, title: str, user_id: int ) -> Tasks:
        new_task = Tasks(title, user_id)
        self.session.add(new_task)
        self.session.commit()
        return  {
        "id": new_task.id,
        "title": new_task.title,
        "done": new_task.done
    }
    
    def list_tasks(self, user_id) -> list[Tasks]:
        tasks = self.session.query(Tasks).filter(Tasks.user_id == user_id).all()
        return tasks
    
    def update_tasks(self, task_id: int, user_id: int, title: str = None, done: bool = None):
        task = self.session.query(Tasks).filter(Tasks.id == task_id).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task Not Found")
        if task.user_id != user_id:
            raise HTTPException(status_code=403, detail="You Don't Have Permission To Edit This Task")
        
        if title is not None:
            task.title = title
        if done is not None:
            task.done = done
        self.session.commit()

        return task
    
    def delete_tasks(self, task_id, user_id) -> None:
        del_task = self.session.query(Tasks).filter(Tasks.id == task_id)

        if not del_task:
            raise HTTPException(status_code=404, detail="Task Not Found")
        if del_task.user_id != user_id:
            raise HTTPException(status_code=403, detail="You Don't Have Permission To Delete This Task")
        
        self.session.delete(del_task)
        self.session.commit()
        return {"message": "task deleted!"}

