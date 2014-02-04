from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('protocol_submission.html')

if __name__ == '__main__':
    app.run()
