import sqlite3 


class Database:
    def Listar_botoes(self):

        conexao = sqlite3.connect("deck.db")

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM buttons")

        dados = cursor.fetchall()

        for registro in dados:
            print("Regitros do banco!: ")

            print("--------------------")
            print("ID:", registro[0])
            print("NOME:", registro[1])
            print("TIPO:", registro[2])
            print("AÇÃO:", registro[3])
            print("--------------------")

        conexao.close


    def inserir_botao(self, nome, tipo, acao):

        conexao = sqlite3.connect("deck.db")

        cursor = conexao.cursor()

        cursor.execute("INSERT INTO buttons" \
        "(nome, tipo, acao)" \
        "VALUES (?, ?, ?)", (nome, tipo, acao))
    
        conexao.commit()
        conexao.close()



    def editar_botao(self, id_botao, nome, tipo, acao):

        conexao = sqlite3.connect("deck.db")

        cursor = conexao.cursor()

        cursor.execute("UPDATE buttons SET nome = ?, tipo = ?, acao = ? WHERE id = ?",
                        (nome, tipo, acao, id_botao))

        conexao.commit()
        conexao.close()

    def deletar_botao(self, id_botao):
        conexao = sqlite3.connect("deck.db")

        cursor = conexao.cursor()

        cursor.execute("DELETE FROM buttons WHERE id = ?", (id_botao,))

        conexao.commit()
        conexao.close()