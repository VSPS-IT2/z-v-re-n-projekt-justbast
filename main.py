from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder="templates", static_folder="static")


todos = [{"úkol": "Ukázkový úkol", "hotovo": False}]

#zobrazení seznamu úkolů
@app.route("/")
def index():
    # Vrátí obsah šablony 'index.html' s proměnnou 'todos' jako kontext
    return render_template("index.html", todos=todos)

#přidání úkolu
@app.route("/přidat", methods=["POST"])
def add():
    úkol = request.form['úkol']
    todos.append({"úkol": úkol, "hotovo": False})
    return redirect(url_for("index"))

#označení úkolu jako hotový
@app.route("/označit-jako-hotovo/<int:index>")
def check(index):
    todos[index]['hotovo'] = not todos[index]['hotovo']

    return redirect(url_for("index"))

# smazání úkolu
@app.route("/smazat/<int:index>")
def delete(index):
    # Smazání úkolu ze seznamu
    del todos[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)