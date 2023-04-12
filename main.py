import uvicorn
from fastapi import FastAPI
from typing import List
from src.models import User,Post
from src.database import get_posts, get_users, add_user, add_post

app = FastAPI()

@app.get('/users',response_model=List[User])
def getUsers(offset:int = 0,limit:int=None):
    return get_users(offset,limit)

@app.get('/posts/{user_id}',response_model=List[Post])
def getPosts(user_id:int,offset:int = 0,limit:int=None):
    return get_posts(user_id,limit,offset)

@app.post('/users')
def addUser(user:User):
    return add_user(user)

@app.post('/posts/')
def addPost(post:Post):
    return add_post(post)


if __name__ == "__main__":
    uvicorn.run('myapp:app', log_level="debug", reload=True)