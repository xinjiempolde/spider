from flask import Flask
from flask import render_template, redirect, url_for, request, session, make_response, g
import time

app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            response = make_response('No such user!')
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)

    return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

app.secret_key = '123456'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)