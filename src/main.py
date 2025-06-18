from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool

tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    """
    Create a new task
    """
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    """
    Get all tasks
    """
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """
    Get a specific task by id
    """
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    """
    Update a specific task by id
    """
    for tsk in tasks:
        if tsk.id == task_id:
            tsk.title = task.title
            tsk.description = task.description
            tsk.done = task.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a specific task by id
    """
    for tsk in tasks:
        if tsk.id == task_id:
            tasks.remove(tsk)
            return {"message": "Task has been deleted successfully!"}
    raise HTTPException(status_code=404, detail="Task not found")