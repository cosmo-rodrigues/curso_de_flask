# Aula 6 - Métodos HTTP
from flask import Flask, request

app = Flask(__name__, static_folder='site')

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == 'POST':
        return "POST"
    return "GET"

if __name__ == '__main__':
    app.run(debug=True)