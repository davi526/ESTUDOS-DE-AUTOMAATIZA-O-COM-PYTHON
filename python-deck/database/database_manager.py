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

    def atualizar_botao(self, id_botao, nome, tipo, acao):
        """Atualiza um botão existente e preserva seu ID."""
        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()

        try:
            cursor.execute(
                """
                UPDATE buttons
                SET nome = ?, tipo = ?, acao = ?
                WHERE id = ?
                """,
                (nome, tipo, acao, id_botao)
            )
            conexao.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as erro:
            print("ERRO AO ATUALIZAR ATALHO:", erro)
            conexao.rollback()
            return False
        finally:
            cursor.close()
            conexao.close()