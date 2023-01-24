from flask import redirect, url_for, render_template
from view import app

@app.route("/")
def root():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)