from flask import Flask
app = Flask(__name__)

posts = []

@app.route("/")
def index():
    return "{} posts".format(len(posts))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
