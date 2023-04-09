from datetime import datetime

from sqlalchemy import MetaData,Integer,String,TIMESTAMP,ForeignKey,Table,Column


metadata = MetaData()

Users = Table(
    "tblUsers",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String,nullable=False),
    Column("username",String,nullable=False),
    Column("job",String,nullable=False),
    Column("photo",String,nullable=False),
)

Posts = Table(
    "tblPosts",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("id_user",Integer,ForeignKey("tblUsers.id")),
    Column("title",String,nullable=False),
    Column("description",String,nullable=False),
    Column("date",TIMESTAMP,default=datetime.utcnow),
)