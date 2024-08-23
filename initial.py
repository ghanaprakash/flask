from flask import Flask , render_template


app=Flask(__name__)

@app.route("/")
@app.route("/kg")

def index():
    

    return render_template("first_intro.html")
@app.route("/dfg")
def test():
    return render_template("second_intro.html")

if __name__=="__main__":
    app.run(debug=True)