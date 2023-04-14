import uvicorn
from fastapi import FastAPI,status,HTTPException
from typing import List, Union, Literal
from src.models import User, Post, getUser, getPost
from src.database import get_posts, get_users, add_user, add_post

app = FastAPI()

@app.get('/users',response_model=List[getUser])
def getUsers(
            limit:int=5,
            offset:int = 0,
            orderBy:Union[Literal['DESC'] , Literal['ASC'] ]='ASC',
            OrderField:Union[Literal['id'] , Literal['name'],Literal['username'] ,Literal['job'] ] = 'id'):

    if offset<0:
        raise HTTPException(status_code=400, detail=f"offset must be >=0 but was {offset}")
    if limit < 0:
        raise HTTPException(status_code=400, detail=f"limit must be >=0 but was {limit}")

    res = get_users(limit,offset,orderBy,OrderField)
    return res

@app.get('/posts/{user_id}',response_model=List[getPost])
def getPosts(
        user_id:int,
        offset:int = 0,
        limit:int=5,
        orderBy:Union[Literal['DESC'] , Literal['ASC'] ]='ASC',
        OrderField:Union[Literal['id'] , Literal['title'],Literal['description'] ,Literal['date'] ] = 'id'):

    if offset<0:
        raise HTTPException(status_code=400, detail=f"offset must be >=0 but was {offset}")
    if limit < 0:
        raise HTTPException(status_code=400, detail=f"limit must be >=0 but was {limit}")

    res = get_posts(user_id, limit, offset,orderBy,OrderField)
    return res

@app.post('/users',status_code=status.HTTP_201_CREATED)
def addUser(user:User):
    res = add_user(user)
    return res

@app.post('/posts',status_code=status.HTTP_201_CREATED)
def addPost(post:Post):
    res = add_post(post)
    return res


if __name__ == "__main__":
    uvicorn.run('main:app', log_level="debug", reload=True)