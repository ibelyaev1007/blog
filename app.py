from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello from index"


@app.route('/about')
def about():
    return "Hello from about"


if __name__ == "__main__":
    app.run(debug=True)
