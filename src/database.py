import sqlite3
from src.config import DB_PATH,DB_FILE
from src.models import User,Post


con = sqlite3.connect(f'../ibs.db', check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS "tblUsers" (
    id INTEGER NOT NULL, 
    name VARCHAR NOT NULL, 
    username VARCHAR NOT NULL, 
    job VARCHAR NOT NULL, 
    photo VARCHAR NOT NULL, 
    PRIMARY KEY (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS "tblPosts" (
    id INTEGER NOT NULL, 
    id_user INTEGER, 
    title VARCHAR NOT NULL, 
    description VARCHAR NOT NULL, 
    date TIMESTAMP, 
    PRIMARY KEY (id), 
    FOREIGN KEY(id_user) REFERENCES "tblUsers" (id)
)
)''')
def add_user(user:User):
    cur.execute(f"""INSERT INTO tblUsers VALUES
                ({user.id}, '{user.name}', '{user.username}','{user.job}','{user.photo}')
                """
                )
    con.commit()
    return get_users()

def add_post(post:Post):
    cur.execute(f"""INSERT INTO tblPosts VALUES
                ({post.id},'{post.id_user}', '{post.title}', '{post.description}','{post.date}')
                """
                )
    con.commit()
    return get_posts(post.id_user)

def get_users(offset=0,limit=None):
    if not con:
        return ["error connect"]
    res = []
    q = "SELECT * from tblUsers"

    if limit and  0<limit:
        q+=f" LIMIT {limit}"
    if offset and 0<offset:
        q+=f" OFFSET {offset}"

    for user in cur.execute(q):
        res.append(User(id=user[0],name=user[1],username=user[2],job=user[3],photo=user[4]))
    return res

def get_posts(id_user,limit=None,offset=0) -> list:
    res = []
    q = f"SELECT * from tblPosts WHERE id_user = {id_user}"

    if limit and 0 < limit:
        q += f" LIMIT {limit}"
    if offset and 0 < offset:
        q += f" OFFSET {offset}"

    for post in cur.execute(q):
        res.append(Post(id=post[0],id_user=post[1], title=post[2], description=post[3], date=post[4]))
    return res

