import sqlite3
#        ----------- CREATE TABLES -----------
def create_table():
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS SignUp(name TEXT, email TEXT, password TEXT)")
    con.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS BLOGS_TABLE
                (title TEXT,
                 content TEXT,
                 image TEXT,
                 audio TEXT,
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 time DATETIME DEFAULT CURRENT_TIMESTAMP)""")   
    # cur.execute("DELETE FROM BLOGS_TABLE") 
    con.commit()
    con.close()

# --------------- make an account --------------
def signup_data(name,email,password):
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("INSERT INTO SignUp (name,email,password) VALUES(?,?,?)",(name,email,password))
    con.commit()
    con.close()

#                               -------- BLOGS ---------   
def add_blogs(title,content,image,audio):
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO BLOGS_TABLE (title,content,image,audio) VALUES(?,?,?,?)
                   """,(title,content,image,audio))
    con.commit()
    con.close()

def get_blogs():
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("SELECT id,title,content,image,audio,time from BLOGS_TABLE ORDER BY time DESC")
    x=cur.fetchall()
    con.close()
    return x
    







# import sqlite3
# # from app import login_email,login_password
# def SignUp_Data(NAME,EMAIL,PASSWORD):
#     connection= sqlite3.connect("database.db")
#     pen=connection.cursor()
#     pen.execute("CREATE TABLE IF NOT EXISTS SignUpData (name TEXT, email TEXT, password TEXT) ")
#     pen.execute("INSERT INTO SignUpData VALUES(?,?,?)", (NAME , EMAIL , PASSWORD))
#     # reading_email=pen.execute("SELECT email from SignUpData")
#     # reading_password=pen.execute("SELECT password from SignUpData")
#     # pen.execute("SELECT email , password FROM SignUpData WHERE email=? AND password=? (login_email , login_password)")
#     # user=pen.fetchone()   
#     connection.commit()
#     connection.close()
# def login_data():
#     connection= sqlite3.connect("database.db")
#     pen=connection.cursor()
#     pen.execute("SELECT email , password FROM SignUpData WHERE email=? AND password=?",(login_email , login_password))
#     user=pen.fetchone()
#     connection.close()