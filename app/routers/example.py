# app/routers/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
def read_example():
    return {"example": "response"}

# @router.post("/person_details")
# def create_person_detail():
#     return {"example": "response"}
