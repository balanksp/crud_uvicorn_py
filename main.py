# # app/main.py
# from fastapi import FastAPI ,HttpException
# from pymongo import MongoClient

# app = FastAPI()

# # connect to mongoDB 
# client = MongoClient("mongodb://localhost:27017/")
# db = client["mongodb_database"]
# collection = db["uvicorn_framework"]

#

# @app.post("/person_details/")
# def create_person_detail(details_person):
#  details_person = {
#         "firstname": "John",
#         "lastname": "Doe",
#         "address": [
#             {
#                 "address1": "123456789",
#                 "address2": "!@#$%^&*()_+",
#                 "city": "San Francisco",
#                 "state": "POIUYG",
#                 "pincode": "7885456322",
#             }
#         ],
#         "product": [
#             {
#                 "name": "Product1",
#                 "description": "Description of Product1",
#                 "price": 19.99,
#                 "category": ["Electronics", "Gadgets"],
#             },
#             {
#                 "name": "Product2",
#                 "description": "Description of Product2",
#                 "price": 29.99,
#                 "category": ["Clothing", "Accessories"],
#             },
#         ]
#     }
# result = collection.insert_one(details_person)
# return {"message": "Person details created successfully", "_id": str(result.inserted_id)}

from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["uvicorn_details"]
collection = db["uvicorn_framework"]

class PersonDetails(details_person):
details_person = {
        "firstname": "John",
        "lastname": "Doe",
        "address": [
                        {
                            "address1": "123456789",
                            "address2": "!@#$%^&*()_+",
                            "city": "San Francisco",
                            "state": "POIUYG",
                            "pincode": "7885456322",
                        }
                   ],
        "product": [
                        {
                            "name": "Product1",
                            "description": "Description of Product1",
                            "price": 19.99,
                            "category": ["Electronics", "Gadgets"],
                        },
                        {
                            "name": "Product2",
                            "description": "Description of Product2",
                            "price": 29.99,
                            "category": ["Clothing", "Accessories"],
                        }
        ]
    }

# class PersonDetails(BaseModel):
#     firstname: str
#     lastname: str
#     address: list
#     product: list

 #Define FastAPI Endpoints to Interact with MongoDB:
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define FastAPI Endpoints to Interact with MongoDB:
# @app.post("/person_details/")
# def create_person_detail():
#     result = collection.insert_one(details_person)
#     print(result)
#     return {"message": "Person details created successfully"}

# Define FastAPI Endpoints to Interact with MongoDB:
@app.post("/person_details/")
async def create_person_detail(PersonDetails : details_person):
    result = collection.insert_one(PersonDetails.dict())
    print(result)
    return {"message": "Person details created successfully", "_id": str(result.inserted_id)}


