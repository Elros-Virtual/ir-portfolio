from flask import Flask

app = Flask(_name_)


@app.route("/")
def home():
    return "This if my first Python website"


if _name_ == "_main_":
    app.run()
