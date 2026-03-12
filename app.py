from flask import Flask, render_template, redirect, request
from model.requisitos import pegar_requisitos, inserir_dados


app= Flask(__name__)

@app.route ("/")
def index_html():
    return render_template("index.html")



@app.route ("/requisitos")
def requisitos_html():
    requisitos = pegar_requisitos ()
    return render_template("requisitos.html", requisitos_html = requisitos)



@app.route("/requisitos", methods= ["POST"])
def dados_post():
    descricao = request.form.get("descricao")
    nivel = request.form.get("nivel")
    valor = request.form.get("valor")
    inserir_dados (descricao, nivel, valor)
    return redirect ("/requisitos")



@app.route("/tb_requisitos/delete")
def deletar():
    return redirect("/requisitos")








if __name__ == "__main__":
    app.run(debug=True)


