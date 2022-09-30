from typing import Any

from pydantic import BaseModel
from pydantic_factories import ModelFactory


class UserModel(BaseModel):
    # json body
    # {
    # 	"username": "string",
    # 	"password": "string",
    # 	"email": "string"
    # }

    username: str
    password: str
    email: str


class UserModelFactory(ModelFactory[Any]):
    __model__ = UserModel

    def __repr__(self):
        return f"{self.__model__}"
