from flask import request
from flask import Flask,url_for
from flask import render_template,session
from flask import make_response,session,redirect
app=Flask(__name__)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user']=request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        response=make_response(render_template('login.html',title1=title),200)
        response.headers['key']='value'
        return response
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
app.secret_key='15508321787'
if __name__=='__main__':
    app.run(debug=True)
