from flask import flash,Flask,redirect,url_for
app=Flask(__name__)
@app.route('/')
def hello():
    return redirect(url_for('index'))
@app.route('/login')
def index():
    flash('this is a test')
if __name__=='__main__':
    app.run(debug=True)