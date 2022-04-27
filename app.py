from flask import Flask, request, render_template, views
from view import views

# starting shit

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
