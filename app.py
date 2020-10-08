from flask import Flask, render_template

app = Flask(__name__)

# URL route in flask app

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post one'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post two'
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts")
def posts():
    return render_template("posts.html", posts=all_posts)


@app.route("/home/<string:name>", methods=['GET'])
def greet(name):
    return "Hello, " + name


if __name__ == "__main__":
    app.run(debug=True)
