from flask import Blueprint, render_template, request
import math

views = Blueprint(__name__, "views")


# show shit
@views.route("/nCr")
def math():
    return render_template("index.html")


@views.route('/nCr', methods=['POST'])
def math_POST():
    text = request.form['text']
    text2 = request.form['text2']
    processed_text = text.upper()
    processed_text2 = text2.upper()

    return processed_text + processed_text2



@views.route("/")
def home():
    return render_template("show.html", sum=sum)


# logic here
num1 = 32453
num2 = 233412

sum = num1 + num2

print(sum)

