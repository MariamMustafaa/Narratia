from flask import Flask , render_template , request , flash , session , redirect ,url_for
from data import create_table , signup_data
app=Flask(__name__)
create_table()
app.secret_key="m7XVX5azO0/3Kte|4"
@app.route("/", methods=["POST" ,"GET"])
def sign_up():
    session["user"]=False
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        if not name.strip():
            flash("Name is required!")
            return redirect(url_for("sign_up"))
        elif not email.strip():
            flash("Email is required!")
            return redirect(url_for("sign_up"))
        elif not password.strip():
            flash("password is required!")
            return redirect(url_for("sign_up"))
        elif len(password)<8: 
            flash("Password must be at least 8 characters!") 
            return redirect(url_for("sign_up"))
        signup_data(name=name,email=email,password=password)
        session["user"]=True
    return render_template("signup.html")
@app.route("/login" ,methods=["POST","GET"])
def login():
    return render_template("login.html")

if __name__ =="__main__":
    app.run(debug=True)