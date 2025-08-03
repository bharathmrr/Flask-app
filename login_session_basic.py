from flask import Flask,request,url_for,session,Response,redirect

app=Flask(__name__)
app.secret_key='super123'


@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='admin' and password=='123':
            session['user']=username
            return redirect(url_for('welcome'))
        else:
            return Response("INVALID CREDENTAILSNS",mimetype='text/plain')
    return """
<h2>login page</h2>
<form method="POST"> 
username:<input type='text' name="username"><br>
password:<input type="text" name="password"><br>
<input type='submit' >login
</form>

"""
@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f""" 
<h2>welocme,{session['user']}</h2>
<a href={url_for('logout')}>logout</a>

"""
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run()