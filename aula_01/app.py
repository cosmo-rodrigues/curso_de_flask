from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Index"

@app.route("/teste")
def test():
  return "Teste"

if __name__ == '__main__':
  app.run()