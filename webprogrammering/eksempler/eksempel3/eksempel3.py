from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    værdi = request.args['value']
    tekst = request.args['text']
    return render_template('index.html', v = værdi, t = tekst)

if __name__ == "__main__":
    app.run(debug=True)
