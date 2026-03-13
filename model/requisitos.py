from database.conexao import conectar 

def pegar_requisitos():
    conexao, cursor = conectar()
    cursor.execute("SELECT cod_requisito, descricao, nivel, valor, situacao FROM tb_requisitos")
    requisitos = cursor.fetchall()

    conexao.close()
    return requisitos


def inserir_dados (descricao, nivel, valor):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO tb_requisitos (descricao, nivel, valor, situacao)
                        VALUES (%s, %s, %s, %s)""",
                        [descricao, nivel, valor, 'Pendente'])
    

    conexao.commit()
    conexao.close()



def deletar(codigo: int):
     
    conexao, cursor = conectar()
    cursor.execute ("DELETE FROM tb_requisitos WHERE cod_requisito = %s", [codigo])
    conexao.commit()
    conexao.close()



def situacao(codigo:int, situacao:str):
    conexao, cursor = conectar()
    cursor.execute ("UPDATE tb_requisitos SET situacao = %s WHERE cod_requisito = %s",  [situacao, codigo])

    conexao.commit()
    conexao.close()
    
        