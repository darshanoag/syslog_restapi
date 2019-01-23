import sys
sys.path.append('/ws/dhavnoor-bgl/flask_pkg/lib/python2.7/site-packages')
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='bgl-ads-523',debug=True)
