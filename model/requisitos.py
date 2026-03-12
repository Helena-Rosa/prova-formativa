from database.conexao import conectar 

def pegar_requisitos():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM  tb_requisitos")
    requisitos = cursor.fetchall()

    conexao.close()
    return requisitos


def inserir_dados (descricao, nivel, valor):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO tb_requisitos (descricao, nivel, valor)
                        VALUES (%s, %s, %s)""",
                        (descricao, nivel, valor))
    

    conexao.commit()
    conexao.close()



def deletar(codigo):
     
    conexao, cursor = conectar()
    cursor.execute("""
                    ?????????????
                    """, [codigo])
    conexao.commit()
    conexao.close()
        