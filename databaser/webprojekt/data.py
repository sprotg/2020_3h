from flask import g
import sqlite3

class Data():

    def __init__(self):
        self.DATABASE = 'my_data.db'

        self._create_db_tables()
        c = self._get_db().cursor()

        #Test af brugerprofiler ved opstart
        c.execute("SELECT * FROM UserProfiles;")
        for u in c:
            print(u)


    def _get_db(self):
        db = g.get('_database', None)
        if db is None:
            db = g._databdase = sqlite3.connect(self.DATABASE)
        return db

    def close_connection(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()


    def register_user(self, email, pw):
        db = self._get_db()
        c = db.cursor()
        c.execute("SELECT * from UserProfiles WHERE email = ?", [email])
        r = c.fetchone()
        res = False
        if r is not None:
            #The email is already in use
            res = False
        else:
            c.execute("INSERT INTO UserProfiles (email, password) VALUES (?,?)", [email,pw])
            db.commit()
            res = True
        return res

    def get_user_list(self):
        l = []
        c = self._get_db().cursor()
        c.execute('SELECT * FROM UserProfiles;')
        for u in c:
            l.append("Navn: {}, email: {}, pw: {}".format(u[1],u[2],u[3]))
        return l

    def get_user_id(self, s):
        c = self._get_db().cursor()
        c.execute("SELECT id FROM UserProfiles WHERE email = ?", [s])
        r = c.fetchone()
        #If the user doesn't exist, the result will be None
        if r is not None:
            return r[0]
        else:
            return None

    def login_success(self, email, pw):
        c = self._get_db().cursor()
        c.execute("SELECT password FROM UserProfiles WHERE email = ?", [email])
        r = c.fetchone()
        if r is not None:
            db_pw = r[0]
        else:
            return False
        return db_pw == pw



    def _create_db_tables(self):
        db = self._get_db()
        c = db.cursor()
        try:
            c.execute("""CREATE TABLE UserProfiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                password TEXT);""")
        except Exception as e:
            print(e)

        db.commit()
        return 'UserProfiles table created'
