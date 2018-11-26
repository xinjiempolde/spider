from flask import request
from flask import Flask
app=Flask(__name__)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return 'this is a POST method'
    else:
        return 'this is a GET method'
if __name__=='__main__':
    app.run(debug=True)