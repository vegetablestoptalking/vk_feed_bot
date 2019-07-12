import sqlite3 as sql
from config_bot import token_vk
query = ''
class sql_bot:

    def auth(self, login, code, id):
        db = sql.connect('user.db')
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE login = :login AND password = :password AND chatid is null", {"login": login, "password": code})
        result = cur.fetchall()
        #flag = True if ((code == '') and (login == '')) else False #rewrite with sql
        if len(result) == 0:
            db.close()
            return False
        else:
            cur.execute("UPDATE users SET chatid = :id WHERE login = :login", {"login": login, "id": id})
            db.commit()
            db.close()
            #adding id in db
            return True

    def check_id(self, id):
        db = sql.connect('user.db')
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE chatid = :id", {"id": id})
        result = cur.fetchall()
        return True if len(result) == 1 else False

    def get_token_vk(self, id): #id for new futures
        # add implementation for parsing from sql for everyone
        return token_vk








