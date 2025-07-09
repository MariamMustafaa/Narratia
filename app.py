from  flask import Flask,render_template

narratia=Flask(__name__) #object from flask class to create yhe main server 

@narratia.route("/")

def main():
    return render_template("index.html")

if __name__ == "__main__": # don’t import and run the server from other files only from this file
    narratia.run(debug=True)   
