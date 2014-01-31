from flask import Flask
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return json.dumps({'test': 'value'})


if __name__ == '__main__':
    app.run()
