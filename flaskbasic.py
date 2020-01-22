from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Enter the word and see the result</h1>"

@app.route('/puppyname/<name>')
def namex(name):

    pupname=''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'

    return "<h1> The new word is : {}".format(pupname)

if __name__=='__main__':
    app.run()
