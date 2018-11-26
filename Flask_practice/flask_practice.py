from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):#如果没有参数传递，则使用默认值None
    if name ==None:
        name = 'World'
    return 'Hello %s' % name
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)