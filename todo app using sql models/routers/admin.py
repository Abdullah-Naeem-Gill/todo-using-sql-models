from fastapi import APIRouter, Depends, HTTPException
from deps import get_current_admin
from models import create_user, create_task
from auth import get_password_hash

router = APIRouter()

@router.post("/admin/create-user")
def admin_create_user(name: str, email: str, password: str, current_admin: dict = Depends(get_current_admin)):
    hashed_password = get_password_hash(password)
    role_id = 2  # Default role (User)
    create_user(name, email, hashed_password, role_id)
    return {"msg": "User created"}

@router.post("/admin/assign-task")
def admin_assign_task(task_id: int, user_id: int, current_admin: dict = Depends(get_current_admin)):
    create_task_assignment(task_id, user_id, current_admin['id'])
    return {"msg": "Task assigned"}
