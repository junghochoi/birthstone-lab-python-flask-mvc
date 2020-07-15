# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        print(request.form)
        month = request.form["month"].strip().lower()
        gemstone = model.birthstones[month]
        blood_type = request.form["blood-type"]
        description = model.blood_type[blood_type]
        # print(blood_type)
        return render_template('results.html', month=month, gemstone=gemstone, blood_type=blood_type, description=description)
    else:
        return "You have to use a post method"

