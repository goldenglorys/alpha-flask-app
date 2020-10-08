from flask import Flask

app = Flask(__name__)

# URL route in flask app


@app.route("/")
def hello():
    return "Hello Flask!"


if __name__ == "__main__":
    app.run(debug=True)
