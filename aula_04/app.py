# Aula 4 - Arquivos estáticos
from flask import Flask

app = Flask(__name__, static_folder='site')

if __name__ == '__main__':
    app.run(debug=True)