import sqlite3
from src.models import User,Post,getUser,getPost


con = sqlite3.connect(f'ibs.db', check_same_thread=False)
cur = con.cursor()

# На хостинге не было доступа к консоли чтобы происвести миграции и настройку
cur.execute('''CREATE TABLE IF NOT EXISTS "tblUsers" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR NOT NULL, 
    username VARCHAR NOT NULL, 
    job VARCHAR NOT NULL, 
    photo VARCHAR NOT NULL
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS "tblPosts" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_user INTEGER, 
    title VARCHAR NOT NULL, 
    description VARCHAR NOT NULL, 
    date TIMESTAMP, 
    FOREIGN KEY(id_user) REFERENCES "tblUsers" (id)
)''')

def add_user(user:User):
    cur.execute(f"""INSERT INTO tblUsers VALUES
                ( NULL ,'{user.name}', '{user.username}','{user.job}','{user.photo}')
                """
                )
    con.commit()
    return get_users(limit=1,orderBy='DESK')

def add_post(post:Post):
    cur.execute(f"""INSERT INTO tblPosts VALUES
                (NULL ,'{post.id_user}', '{post.title}', '{post.description}','{post.date}')
                """
                )
    con.commit()
    return get_posts(post.id_user,limit=1,orderBy='DESK')

def get_users(limit=5,offset=0,orderBy='ASC',OrderField='id'):
    res = []
    q = f"SELECT * from tblUsers ORDER BY {OrderField} {orderBy} LIMIT {limit}  OFFSET {offset}"

    for user in cur.execute(q):
        res.append(getUser(id=user[0],name=user[1],username=user[2],job=user[3],photo=user[4]))
    return res

def get_posts(id_user,limit=5,offset=0,orderBy='ASC',OrderField='id') -> list:
    res = []
    q = f"SELECT * from tblPosts WHERE id_user = {id_user} ORDER BY {OrderField} {orderBy} LIMIT {limit} OFFSET {offset} "

    for post in cur.execute(q):
        res.append(getPost(id=post[0],id_user=post[1], title=post[2], description=post[3], date=post[4]))
    return res

