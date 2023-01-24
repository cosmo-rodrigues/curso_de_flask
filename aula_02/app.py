from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index"

def teste_01():
  return "<p>Teste 01</p>"

def teste_02():
  return "<h1>Teste 02</h1>"

app.add_url_rule("/teste", "teste", teste_01)
app.add_url_rule("/teste2", "teste2", teste_02)

if __name__ == '__main__':
  app.run(debug=True, port="3000")
