from flask import Flask
import requests
import json
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/get')
def get():
    uri = 'http://api.open-notify.org/astros.json'
    try:
        global res
        res = requests.get(uri)
        return "Data Fetched"
    except:
        return False
    return res

@app.route('/result')
def result():
    get()
    try:
        print(res)
        result = res.json()
        text = json.dumps(result, sort_keys=True, indent=4)
        name = text.split()[2]
        return "the result is: {}".format(name)
    except:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0')

