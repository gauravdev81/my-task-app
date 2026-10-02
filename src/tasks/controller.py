from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title=data["title"], description=data["description"], is_completed=data["is_completed"])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)


    # return{
    #     "status": "Task Created Successfully",
    #     "data": new_task
    # }

    return new_task

def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    # return {
    #     "status":"All Tasks",
    #     "data": tasks
    # }

    return tasks

def get_one_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)

    if not one_task:
        raise HTTPException(404, detail="Task Id doesn't exist")

    return one_task
	
	# return {
	# 	"status": "Task Fetched Successfully",
	# 	"data": one_task
	# }
    

def update_task(task_id:int, body:TaskSchema, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(401, detail="Task Id doesn't exist")
    
    data = body.model_dump()
    # below 3 lines the way to update the task object with new data from the request body.
    # task.title = data["title"]
    # task.description = data["description"]
    # task.is_completed = data["is_completed"]

    # another short approach - we can upadte 1 or all fields
    for key, value in data.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "status": "Task Updated Successfully",
        "data": task
    }

def delete_task(task_id:int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail="Task Id doesn't exist")
    
    db.delete(task)
    db.commit()

    # return {
    #     "status": "Task Deleted Successfully",
    #     "data": task
    # }
    return None