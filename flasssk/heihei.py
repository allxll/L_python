from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/<name>', methods=['GET', 'POST'])
def home(name):
    return render_template('home.html', name=name)


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password']:
        return render_template('signin-ok.html', username=request.form['username'])
    return render_template('form.html', message='Bad username or password', username=request.form['username'])


if __name__ == '__main__':   app.run(debug=True)
