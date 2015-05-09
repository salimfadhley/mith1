
PAGES = [
    {"title": "Getting Started", "url": "getting-started.html"},
    {"title": "Documentation", "url": "mithril.html"},
    {"title": "Mithril Blog", "url": "http://lhorie.github.io/mithril-blog/"},
    {"title": "Mailing List", "url": "https://groups.google.com/forum/#!forum/mithriljs"}
]

import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return open("templates/index.html").read()

@app.route("/style.css")
def style():
    return open("templates/style.css").read()


@app.route("/pages.json")
def pages():
    return json.dumps(PAGES)

if __name__ == "__main__":
    app.run()