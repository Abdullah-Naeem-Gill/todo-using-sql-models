import sqlite3
from datetime import datetime
from database import get_db_connection

# Role model
def create_role(name: str):
    conn = get_db_connection()
    with conn:
        conn.execute(
            'INSERT INTO roles (name, created_at, updated_at) VALUES (?, ?, ?)',
            (name, datetime.utcnow(), datetime.utcnow())
        )
    conn.close()

def get_role_by_name(name: str):
    conn = get_db_connection()
    role = conn.execute('SELECT * FROM roles WHERE name = ?', (name,)).fetchone()
    conn.close()
    return role

# User model
def create_user(name: str, email: str, hashed_password: str, role_id: int):
    conn = get_db_connection()
    with conn:
        conn.execute(
            'INSERT INTO users (name, email, hashed_password, role_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)',
            (name, email, hashed_password, role_id, datetime.utcnow(), datetime.utcnow())
        )
    conn.close()

def get_user_by_email(email: str):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()
    return user

# Task model
def create_task(title: str, description: str, status: str, created_by: int):
    conn = get_db_connection()
    with conn:
        conn.execute(
            'INSERT INTO tasks (title, description, status, created_by, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)',
            (title, description, status, created_by, datetime.utcnow(), datetime.utcnow())
        )
    conn.close()

def get_tasks_by_user(user_id: int):
    conn = get_db_connection()
    tasks = conn.execute('''
        SELECT tasks.* FROM tasks
        JOIN task_assignments ON tasks.id = task_assignments.task_id
        WHERE task_assignments.user_id = ?
    ''', (user_id,)).fetchall()
    conn.close()
    return tasks
