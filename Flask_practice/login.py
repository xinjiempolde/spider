from flask import request
from flask import Flask
from flask import render_template,session
app=Flask(__name__)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)
app.secret_key='15508321787'
if __name__=='__main__':
    app.run(debug=True)