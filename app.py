from flask import Flask
from flask import render_template
from flask import request
from flask import flash #flash is a function
from data import SignUp_Data , login_data , user 
# from data import reading_email
# from data import reading_password

narratia=Flask(__name__) #object from flask class to create yhe main server 
narratia.secret_key ="m7XVX5azO0/3Kte|4"
@narratia.route("/")
def main():
    return render_template("index.html")

@narratia.route("/signup.html",methods=["POST" , "GET"])
def signup():   

    if request.method=="POST":
        Name=request.form["name"]
        Email=request.form["email"]
        Password=request.form["password"]
        
        # if len(Password)<8:
        #     return("Password must be at least 8 characters!")
        if not Name.strip():
            # return "Name is required!"
            # return render_template("signup.html",nr="Name is required!")
            flash("Name is required!")
            return render_template("signup.html")
        elif not Email.strip():
            # return "Email is required!"
            # return render_template("signup.html",er="Email is required!")
            flash("Email is required!")
            return render_template("signup.html")
        elif not Password.strip():
            # return "Password is required!"
            # return render_template("signup.html",pr="Password is required!")
            flash("Password is required!")
            return render_template("signup.html")
        if len(Password)<8:
            # return render_template("signup.html",pl="Password must be at least 8 characters!")
            flash("Password must be at least 8 characters!")
            return render_template("signup.html")
        SignUp_Data(NAME=Name ,EMAIL=Email ,PASSWORD=Password) 
        
        # message=f"Welcome in Narratia, {Name}"
        # return f"Welcome, {Name}"
        # return render_template("index.html" , message=message)
        flash(f"Welcome in Narratia, {Name}")
        return render_template("index.html")
    return render_template("signup.html")

@narratia.route("/login.html",methods=["POST" , "GET"])
def login():
    if request.method=="POST":
        login_email=request.form["email"]
        login_password=request.form["password"]
        # for row in reading_email:
        #     if row==email:
        #         for row in reading_password:
        #             if password==row:
        #                 return render_template("index.html")
        if user:
            return render_template("index.html")
    
if __name__ == "__main__": # don’t import and run the server from other files only from this file
    narratia.run(debug=True, host='0.0.0.0', port=5000) 
    
