from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route("/about")
def about():
    return "This is the About page!"

if __name__ == '__main__':
    app.run()
