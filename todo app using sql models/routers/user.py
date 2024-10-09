from fastapi import APIRouter, Depends
from deps import get_current_user
from models import get_tasks_by_user

router = APIRouter()

@router.get("/tasks")
def get_user_tasks(current_user: dict = Depends(get_current_user)):
    tasks = get_tasks_by_user(current_user['id'])
    return {"tasks": tasks}

@router.put("/task/{task_id}/status")
def update_task_status(task_id: int, status: str, current_user: dict = Depends(get_current_user)):
    # Logic to update task status here
    pass
