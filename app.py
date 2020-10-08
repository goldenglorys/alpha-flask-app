from flask import Flask, render_template

app = Flask(__name__)

# URL route in flask app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home/<string:name>", methods=['GET'])
def greet(name):
    return "Hello, " + name


if __name__ == "__main__":
    app.run(debug=True)
