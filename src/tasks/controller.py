from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel

def create_task(body:TaskSchema, db:Session, user: UserModel):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"], 
        description=data["description"], 
        is_completed=data["is_completed"],
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)


    # return{
    #     "status": "Task Created Successfully",
    #     "data": new_task
    # }

    return new_task

def get_tasks(db: Session, user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    # return {
    #     "status":"All Tasks",
    #     "data": tasks
    # }

    return tasks

def get_one_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(404, detail="Task Id doesn't exist")

    return one_task
	
	# return {
	# 	"status": "Task Fetched Successfully",
	# 	"data": one_task
	# }
    

def update_task(task_id:int, body:TaskSchema, db:Session, user: UserModel):
    task: TaskModel = db.get(TaskModel, task_id)
    if not task:
        raise HTTPException(404, detail="Task Id doesn't exist")

    if task.user_id != user.id:
        raise HTTPException(403, detail="You are not authorized to update this task")
    
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

    # return {
    #     "status": "Task Updated Successfully",
    #     "data": task
    # }
    return task

def delete_task(task_id:int, db:Session, user: UserModel):
    task = db.get(TaskModel, task_id)
    if not task:
        raise HTTPException(404, detail="Task Id doesn't exist")

    if task.user_id != user.id:
        raise HTTPException(403, detail="You are not authorized to delete this task")
    
    db.delete(task)
    db.commit()

    # return {
    #     "status": "Task Deleted Successfully",
    #     "data": task
    # }
    return None