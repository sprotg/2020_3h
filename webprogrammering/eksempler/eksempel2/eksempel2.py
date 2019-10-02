from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', navn = 'Søren')

@app.route('/side2')
def side2():
    ordliste = ['en', 'lang', 'liste', 'med', 'ord']
    return render_template('side2.html', liste = ordliste)

if __name__ == "__main__":
    app.run(debug=True)
