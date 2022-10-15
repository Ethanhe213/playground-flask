from winsound import PlaySound
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/playground/<int:num>/<string:color>')
def hello(num,color):
    return render_template('playground.html',num=num,color=color)



if __name__=="__main__":
    app.run(debug=True) 