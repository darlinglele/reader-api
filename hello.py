from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='www.baidu.com'>Hello World!</a>"

if __name__ == "__main__":
    app.run()
