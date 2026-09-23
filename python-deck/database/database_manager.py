import sqlite3

from database.db import CAMINHO_BANCO


class Database:

    def inserir_botao(self, nome, tipo, acao):

        # Abre uma conexão com o banco oficial
        conexao = sqlite3.connect(CAMINHO_BANCO)

        try:
            # Cria o cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Insere o novo atalho
            cursor.execute(
                """
                INSERT INTO buttons (nome, tipo, acao)
                VALUES (?, ?, ?)
                """,
                (nome, tipo, acao)
            )

            # Confirma a operação
            conexao.commit()

        finally:
            # Garante o fechamento mesmo se ocorrer algum erro
            conexao.close()

    def listar_botoes(self):

        # Abre uma conexão com o banco oficial
        conexao = sqlite3.connect(CAMINHO_BANCO)

        try:
            # Cria o cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Consulta todos os botões cadastrados
            cursor.execute(
                """
                SELECT id, nome, tipo, acao
                FROM buttons
                ORDER BY id
                """
            )

            # Entrega os registros para quem chamou o método
            return cursor.fetchall()

        finally:
            # Garante o fechamento mesmo se ocorrer algum erro
            conexao.close()