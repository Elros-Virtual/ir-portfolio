from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql.functions import user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<name %r>' % self.id


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


@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        name = request.form.get("name")
        new_user = users(name=name)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/register')
        except:
            return "There was an error"

    else:
        user_list = users.query.order_by(users.date_created)
        return render_template('register.html', user_list=user_list)


# @app.route('/update/<int:id>', methods=["POST", "GET"])
# def update_user(id):
#     user_to_update = users.query.get_or_404(id)
#     if request.method == "POST":
#         user_to_update = request.form('name')
#         try:
#             db.session.commit()
#             return redirect('/register')
#         except:
#             return "there was an error"
#     return render_template('myaccount.html', user_to_update=user_to_update)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
