from flask import Flask
import os

app = Flask(__name__, static_folder='static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')


@app.route('/')
def hello_world():
    with open(os.path.join(APP_ROOT, 'abc.txt')) as fil:
        data = fil.read()
        return 'Hello World!' + data


if __name__ == '__main__':
    app.run(debug=True)
