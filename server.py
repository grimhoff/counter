from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="papa bear"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/clear')
def clear():
        session.clear()
        return redirect('/')


if __name__=="__main__":
    app.run(debug=True)