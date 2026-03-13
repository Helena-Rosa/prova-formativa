from flask import Flask, render_template, redirect, request
from model.requisitos import pegar_requisitos, inserir_dados, deletar, situacao


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



@app.route("/requisitos/delete/<codigo>")
def pg_deletar(codigo):
    deletar(codigo)
    return redirect("/requisitos")



@app.route("/requisitos/situacao_pendente/<codigo>")
def situacao_pendente (codigo):
    situacao (codigo, 'Pendente')
    return redirect ("/requisitos")


@app.route("/requisitos/situacao_resolvido/<codigo>")
def situacao_resolvido (codigo):
    situacao (codigo, 'Resolvido')
    return redirect ("/requisitos")







if __name__ == "__main__":
    app.run(debug=True)


