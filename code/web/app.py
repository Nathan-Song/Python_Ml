from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"name": "my_app"}), 200


@app.route("/login")
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    if email == "info@kodschul.com" and password == "kodschul.com":
        return render_template("profile.html", name="Welcome back!")

    return render_template("login.html")


@app.route("/user/<username>")
def show_user(username):

    return render_template("profile.html", name=username)
    # return f"<h1>Hello {username}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
