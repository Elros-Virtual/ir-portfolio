from flask import Flask, render_template, request
from flask.helpers import url_for


app = Flask(__name__)


@app.route("/")
def index():
    title = "home page"
    return render_template('home.html', title=title)


@app.route("/skills")
def skills():
    return render_template('skills.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/tech-blog")
def techblog():
    return render_template('techblog.html')


@app.route("/workexperience")
def work():
    return render_template('work.html')


@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')


@app.route("/business")
def business():
    return render_template('business.html')


@app.route("/subscribe", methods=["POST", "GET"])
def subscribe():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        error_statement = "All form fields required"
        return render_template('subscribe.html', error_statement=error_statement, name=name, email=email)

    return url_for('/form')


@app.route("/form", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    return render_template('form.html', name=name, email=email)


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
