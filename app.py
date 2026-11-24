from flask import Flask, abort, render_template

app = Flask(__name__)

articles = [
    {"id": 1, "title": "Getting Started",
     "content": "This is our first article."},
    {"id": 2, "title": "Keep Building",
     "content": "Small steps add up."},
]

@app.route("/")
def home():
    return render_template("home.html", heading="Articles", articles=articles)

@app.route("/articles/<int:article_id>")
def article_detail(article_id):
    for article in articles:
        if article["id"] == article_id:
            return render_template("article-detail.html", article=article)
    abort(404)
