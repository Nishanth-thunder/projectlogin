# this is login page
from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home():
    return render_template("log.html")
@app.route("/process",methods=['GET','POST'])
def proc():

    if request.method=="POST" and 'user' in request.form:
        c=0
        u=request.form.get('user')
        p=request.form.get('password')
        con = sqlite3.connect("ntt.db")
        cur = con.cursor()
        query = "Select name,phnumber from emp"
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        con.close()
        for d in data:
            if d[0]==u and d[1]==p:
                c=1
                return render_template("page.html")
            else:
                c=0
        if c==0:
            return "INCORRECT LOGIN ATTEMPTED"


@app.route("/register",methods=['GET','POST'])
def ho():
    return render_template("reg.html")
@app.route("/reg",methods=['GET','POST'])
def rom():
    nu = ""
    n = ""
    t = ""
    f = ""

    if request.method == "POST" and 'name' in request.form:
        nu = request.form.get('phnumber')
        n = request.form.get('name')
        t = request.form.get('role')
        f = request.form.get('address')
    con = sqlite3.connect("ntt.db")
    con.execute("Insert into emp('phnumber','name','role','address')values(?,?,?,?)", [nu, n, t, f])
    con.commit()
    con.close()
    return "YOU HAVE REGISTERED SUCESSFULLY ! YOUR NAME AND PHONE NUMBER WILL BE YOUR USERNAME AND PASSWORD"
app.run()
