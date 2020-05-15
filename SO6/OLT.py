from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'very secret string'

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        pass

    app.run(debug=True)
