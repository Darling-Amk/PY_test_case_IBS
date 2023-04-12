import sqlite3
from src.config import DB_PATH,DB_FILE
from src.models import User,Post


con = sqlite3.connect(f'{DB_PATH}/{DB_FILE}', check_same_thread=False)
cur = con.cursor()


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

