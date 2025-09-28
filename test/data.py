import sqlite3

def create_table():
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS SignUp(name TEXT, email TEXT, password TEXT)")
    con.commit()
    con.close()

def signup_data(name,email,password):
    con=sqlite3.connect("database.db")
    cur=con.cursor()
    cur.execute("INSERT INTO SignUp (name,email,password) VALUES(?,?,?)",(name,email,password))
    con.commit()
    con.close()

