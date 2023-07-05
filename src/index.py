from flask import Flask
import hello

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><button onclick='this.parentElement.append(\"Click\")'>Add</button>"


@app.route("/user/<username>")
def hello_user(username):
    return hello.say_hello(username)


app.run(host='localhost', port=5000)
