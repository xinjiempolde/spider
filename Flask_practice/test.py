from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    username=request.cookies.get('User-Agent')
    print (username)
if __name__=='__main__':
    app.run(debug=True)