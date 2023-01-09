from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_api="https://api.npoint.io/9ea21f16c24b210444f4"

@app.route('/')
def home():
    response=requests.get(blog_api)
    all_post=response.json()
    return render_template("index.html",all_post=all_post)

@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    response=requests.get(blog_api)
    content=response.json()
    for dict in content:
        if dict["id"]==blog_id:
            post=dict

    return render_template('post.html',post=post)


if __name__ == "__main__":
    app.run(debug=True)
