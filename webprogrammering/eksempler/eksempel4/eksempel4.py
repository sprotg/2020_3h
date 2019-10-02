from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modtag_data', methods = ['POST'])
def modtag():
    t = request.form['in_text']
    return render_template('data.html', data = t)

if __name__ == "__main__":
    app.run(debug=True)
