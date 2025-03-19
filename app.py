from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def homepage():
    context = {}
    context["logo"] = "img/logo_senai.png"
    context["img"] = "img/img_home.png"
    context["Titulo"] = "VENDINHA DA C13"
    context["Texto"] = "Seja Bem vindo a vendinha da C13"
    return render_template("homepage.html", **context)

@app.route('/add_produto')
def add_produto():
    context = {}
    return render_template("add_produto.html", context=context)

@app.route('/del_produto')
def del_produto():
    context = {}
    return render_template("del_produto.html", context=context)

@app.route('/up_produto')
def up_produto():
    context = {}
    return render_template("up_produto.html", context=context)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")