from fastapi import APIRouter, Depends, status, Request, BackgroundTasks
from sqlalchemy.orm import Session
from src.user import controller
from src.utils.db import get_db
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model = UserResponseSchema, status_code = status.HTTP_201_CREATED)
async def register(body: UserSchema, bg_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    return await controller.register(body, db, bg_tasks)

@user_routes.post("/login", status_code = status.HTTP_200_OK)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)

@user_routes.get("/is_auth", status_code = status.HTTP_200_OK, response_model = UserResponseSchema)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return controller.is_authenticated(request, db)
