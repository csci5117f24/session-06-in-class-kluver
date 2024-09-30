from flask import Flask, render_template, redirect, request, url_for
from db import *

app = Flask(__name__)
setup()


@app.route("/")
def hello():
    colors = get_colors()

    return render_template("main.html", colors=colors)


@app.route("/new_color", methods=["POST"])
def new_color():
    color_code = request.form.get("color", "#ffffff")
    color_name = request.form.get("name", "black")
    create_color(color_code, color_name)
    return redirect(url_for("hello"))
