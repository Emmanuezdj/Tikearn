from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    username=request.form["username"]
    password=request.form["password"]
    print("Username:",username,"Password:",password)
    return "<h1>Processing</h1>"
    

if __name__ == '__main__':
    app.run(debug=True)

