import pymongo
import yaml
from bson import ObjectId
from pydantic import BaseModel, Field
from config import MongoConfig

MONGODB_URL = MongoConfig.URL
MONGODB_DB = MongoConfig.DB
MONGODB_USER_TABLE = MongoConfig.USER_TABLE
MONGODB_DATA_TABLE = MongoConfig.DATA_TABLE

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
    admin: bool = Field(...)
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

class Data(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    keyword: str = Field(...)
    classname:  str = Field(...)
    data: dict = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jerry Kim",
                "keyword": "test",
                "classname": "test",
                "data": ["000001.jpg", "000002.jpg"]
            }
        }