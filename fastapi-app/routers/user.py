from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..repository import user

router = APIRouter(
    prefix="/user",
tags=['users']
)

@router.post('/',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser,status_code=status.HTTP_200_OK)
def get_user(id:int,db:Session = Depends(get_db)):
    return user.getUser(id,db)