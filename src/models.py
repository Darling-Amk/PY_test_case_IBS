from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Literal, Union
from sqlalchemy import MetaData,Integer,String,TIMESTAMP,ForeignKey,Table,Column,Identity

metadata = MetaData()


class getUser(BaseModel):
    id: int
    name: str
    username: str
    job: str
    photo: Optional[str] = None

class User(BaseModel):
    name: str
    username: str
    job: str
    photo: Optional[str] = None

class Post(BaseModel):
    id_user: int
    title: str
    description: str
    date: Optional[datetime]

class getPost(BaseModel):
    id: int
    id_user: int
    title: str
    description: str
    date: Optional[datetime]

Users = Table(
    "tblUsers",
    metadata,
    Column("id",Integer,Identity(),primary_key=True),
    Column("name",String,nullable=False),
    Column("username",String,nullable=False),
    Column("job",String,nullable=False),
    Column("photo",String,nullable=False),
)

Posts = Table(
    "tblPosts",
    metadata,
    Column("id",Integer,Identity(),primary_key=True),
    Column("id_user",Integer,ForeignKey("tblUsers.id")),
    Column("title",String,nullable=False),
    Column("description",String,nullable=False),
    Column("date",TIMESTAMP,default=datetime.utcnow),
)