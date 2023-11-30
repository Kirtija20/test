from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1"},
    {"id": 2, "title": "Task 2", "description": "Description 2"},
]

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task_id = max(t["id"] for t in tasks) + 1
    task_dict = task.dict()
    task_dict["id"] = task_id
    tasks.append(task_dict)
    return task_dict

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task_index = next((index for index, t in enumerate(tasks) if t["id"] == task_id), None)
    if task_index is not None:
        tasks[task_index] = updated_task.dict()
        return tasks[task_index]
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task_index = next((index for index, t in enumerate(tasks) if t["id"] == task_id), None)
    if task_index is not None:
        deleted_task = tasks.pop(task_index)
        return deleted_task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.get("/")
def read_root():
    # Example logging
    logging.info("Accessed the root endpoint")
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)





















































'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description for Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Description for Task 2", "completed": True},
]

class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool 

@app.get("/tasks/{task_id}", response_model=dict)
async def read_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
      

@app.put("/tasks/{task_id}", response_model=dict)
async def update_task(task_id: int, updated_task: TaskUpdate):
    """Update a specific task by ID, or raise a 404 error if not found."""
    task_index = next((index for index, t in enumerate(tasks) if t["id"] == 1), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_index].update(updated_task.dict())
    return {"message": f"Task {task_id} updated successfully", "updated_task": tasks[task_index]}

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    task_index = next((index for index, t in enumerate(tasks) if t["id"] == 1), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_index)
    return {"message": f"Task {task_id} deleted successfully", "deleted_task": deleted_task}


@app.get("/tasks", response_model=list)
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=dict)
async def read_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

class Person(BaseModel):
    name: str
    age: int
    email: str

@app.post("/create_person")
async def create_person(person: Person):
    return {"message": f"Person {person.name} created successfully."}

tasks = []

@app.post("/add_task/")
async def add_task(task: str):
    if not task:
        raise HTTPException(status_code=400, detail="Task cannot be empty")

    tasks.append(task)

    return {"message": "Task added successfully"}

@app.delete("/delete_task/{task_id}")
async def delete_task(task_id: int):
    task_index = find_task_index(task_id)
    if task_index == -1:
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks.pop(task_index)
    return {"message": "Task deleted successfully", "deleted_task": deleted_task}

def find_task_index(task_id: int) -> int:
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return i
    return -1



class TaskCreate(BaseModel):
    title: str
    description: str = None


@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/read_tasks")
async def read_tasks():
    return tasks

@app.post("/create_task")
async def create_task(task: TaskCreate):
    new_task = task.dict()
    tasks.append(new_task)
    return new_task
'''
