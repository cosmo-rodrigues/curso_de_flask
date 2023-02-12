# URL dinâmica

from flask import Flask

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<nome>")
def hello(nome = "visitante"):
    return "<h1>Hello, {}</h1>".format(nome)


@app.route("/blog/")
@app.route("/blog/<int:postId>")
def blog1(postId = -1):
      if(postId >= 0):
           return "Blog, post número {}".format(postId)
      return "Blog, página inicial"

if __name__ == '__main__':
    app.run(debug=True)