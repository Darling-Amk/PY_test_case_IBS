# import sqlite3
# con = sqlite3.connect("ibs.db")
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    username: str
    job: str
    photo: Optional[str] = None

class Post(BaseModel):
    id_user: int
    title: str
    description: str
    date: str

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

def get_posts(id_user,limit=None,offset=0,orderby=None) -> list:
    if offset>len(posts):
        return []
    posts_ = posts[offset:]
    res = [post for post in posts_ if post["id_user"]==id_user]
    if limit and len(res)>limit:
        res = res[:limit]
    return res