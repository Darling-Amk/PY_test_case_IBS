from fastapi import FastAPI
from typing import List
from database import get_posts,get_users,User,Post

#uvicorn myapp:app --reload


app = FastAPI()


@app.get('/users',response_model=List[User])
def getUsers():
    return get_users()

@app.get('/posts/{user_id}',response_model=List[Post])
def getPosts(user_id:int,offset:int = 0,limit:int=None):
    return get_posts(user_id,limit,offset)