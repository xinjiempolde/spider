from flask import Flask,abort
app=Flask(__name__)
@app.errorhandler(404)
def wrong():
    return render_template('the page is not found')
if __name__=='__main__':
    app.run(debug=True)