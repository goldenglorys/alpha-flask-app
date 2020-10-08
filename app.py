from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  # tell flask which db is to be used
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self): # this will let know when new post is created through this model
        return 'Blog post ' + str(self.id)

# URL route in flask app


all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post one',
        'author': 'Edward'
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
