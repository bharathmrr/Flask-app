from flask import Flask,render_template,request,Response
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/submit",methods=['POST'])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    if username=="bharath123" and password=="pass":
        return render_template('index.html')
    else:
        return Response("INVALID CREDISTIOAL",mimetype='text/plain')

if __name__=="__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)
