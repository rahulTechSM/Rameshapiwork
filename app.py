from flask import Flask, render_template,request, redirect, url_for
from helpers.page1 import datareturn
app = Flask(__name__)
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/",methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("page1"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/page1")
def page1():
    user= datareturn()
    return render_template("index1.html",user=user)



if __name__ == "__main__":
    app.run(debug=True)