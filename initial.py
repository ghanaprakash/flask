from flask import Flask , render_template,request


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

@app.route("/kg")

def index():
    message=""
    if request.method=="POST":
        if request.form["username"]=="prakash" and request.form["pass"]=="1234":
            message="logged is successfully"
        else:
            message="invalid username amd password"
            
    return render_template("first_intro.html " ,msg=message)
@app.route("/dfg")
def test():
    return render_template("second_intro.html")

if __name__=="__main__":
    app.run(debug=True)