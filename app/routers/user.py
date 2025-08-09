from fastapi import APIRouter, Depends, HTTPException, status

from app.database import SessionLocal
from app.dependencies.auth import verify_token
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.services.user import UserService


router = APIRouter(dependencies=[Depends(verify_token)])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_service(db=Depends(get_db)):
    return UserService(db)


@router.get("/user", response_model=list[UserOut])
def read_users(
    skip: int = 0,
    limit: int = 10,
    service: UserService = Depends(get_user_service),
):
    return service.get_users(skip, limit)


@router.get("/user/{user_id}", response_model=UserOut)
def read_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    db_user = service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/user/", response_model=UserOut)
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service),
):
    db_user = User(name=user.name, phone=user.phone, password_hash=user.password)
    return service.create_user(db_user)


@router.delete("/user/{user_id}")
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    db_user = service.delete_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": f"User {db_user.name} deleted successfully"}
