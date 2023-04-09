from fastapi import FastAPI
from typing import List,Dict
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    username: str
    job: str
    photo: Optional[str] = None

app = FastAPI(

)

db = [
    {
        "id": 1,
        "name": "Иванов",
        "username": "Сергей",
        "job": "Дизайнер",
        "photo": "https://..." ,
    },
    {
        "id": 2,
        "name": "Иванов",
        "username": "Иванович",
        "job": "Программист",
        "photo": "https://...",
    },
]

posts = [
    {
        "id_user":1,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
    {
        "id_user": 1,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
    {
        "id_user": 1,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
    {
        "id_user": 1,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
    {
        "id_user": 1,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
    {
        "id_user": 2,
        "title": "Заголовок поста",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Felis nec platea ipsum ornare interdum. Aliquet metus suscipit ornare aliquet accumsan, massa risus quisque ac. Pellentesque risus mauris mattis viverra amet sed elit. Pellentesque dui vitae amet diam convallis nisi nec.",
        "date": "2023-04-07T15:16:10+00:00"
    },
]

def get_users() -> list:
    return db

def get_posts(id_user) -> list:
    return [post for post in posts if post["id_user"]==id_user]

@app.get('/users')
def getUsers():#->List[User]:
    return get_users()

@app.get('/posts/{user_id}')
def getPosts(user_id:int)->list:
    return get_posts(user_id)