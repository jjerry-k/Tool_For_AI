import os
import pymongo
import yaml
from bson import ObjectId
from pydantic import BaseModel, Field

with open(".cfg/mongo.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

MONGODB_URL = cfg["MONGODB_URL"]
MONGODB_DB = cfg["MONGODB_DB"]
MONGODB_USER_TABLE = cfg["MONGODB_USER_TABLE"]
MONGODB_WORK_TABLE = cfg["MONGODB_WORK_TABLE"]

CLIENT = pymongo.MongoClient(MONGODB_URL)

DB = CLIENT[MONGODB_DB]

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectID")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    permission: bool = Field(...)
    password: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jerry Kim",
                "admin": True,
                "password": "secret_code"
            }
        }