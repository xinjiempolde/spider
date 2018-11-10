from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return ('hello!')
@app.route('/hello')
def hello():
    return ("hhh")
if __name__=='__main__':
    app.run()