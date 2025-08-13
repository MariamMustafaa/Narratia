import sqlite3
# from app import login_email,login_password
def SignUp_Data(NAME,EMAIL,PASSWORD):
    
    connection= sqlite3.connect("database.db")

    pen=connection.cursor()
    pen.execute("CREATE TABLE IF NOT EXISTS SignUpData (name TEXT, email TEXT, password TEXT) ")

    pen.execute("INSERT INTO SignUpData VALUES(?,?,?)", (NAME , EMAIL , PASSWORD))
    # reading_email=pen.execute("SELECT email from SignUpData")
    # reading_password=pen.execute("SELECT password from SignUpData")
    # pen.execute("SELECT email , password FROM SignUpData WHERE email=? AND password=? (login_email , login_password)")
    # user=pen.fetchone()   
    connection.commit()
    connection.close()
def login_data():
    connection= sqlite3.connect("database.db")
    pen=connection.cursor()
    pen.execute("SELECT email , password FROM SignUpData WHERE email=? AND password=?",(login_email , login_password))
    user=pen.fetchone()
    connection.close()
    