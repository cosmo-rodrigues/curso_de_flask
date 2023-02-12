# Aula 04 - COntrução de URLs
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin/")
@app.route("/admin/<name>")
def admin(name = ""):
    if(not name):
        return "<h1>Olá, administrador</h1>"
    return "<p>Olá, {}. Você está logado como administrador.".format(name)

@app.route("/guest/")
@app.route("/guest/<name>")
def guest(name = ""):
    if(not name):
        return "<p>Olá, visitante</p>"
    return "<p>Olá, {}. Você está logado como visitante.".format(name)

@app.route("/user/")
@app.route("/user/<name>")
def user(name = ""):
    if name == "admin":
        return redirect(url_for("admin"))
    return redirect(url_for("guest"))


if __name__ == '__main__':
        app.run(debug=True)