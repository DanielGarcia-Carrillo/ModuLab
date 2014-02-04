from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# TODO: sqlite database setup, we should move over to postgresql later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('base.html')

@app.route('/submit_procedure', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # TODO: take the form parameters and move them into the database
        proc_name = request.form['name']
        return None
    else:
        return render_template('protocol_form.html')

if __name__ == '__main__':
    app.run()
