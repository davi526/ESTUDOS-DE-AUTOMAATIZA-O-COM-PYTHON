# Importa o módulo responsável pelo SQLite
import sqlite3

# Importa Path para criar um caminho absoluto e confiável
from pathlib import Path


# Identifica a pasta onde este arquivo está localizado
PASTA_DATABASE = Path(__file__).resolve().parent

# Define o banco oficial do Python Deck
CAMINHO_BANCO = PASTA_DATABASE / "deck.db"


def inicializar_banco():
    """Cria as tabelas necessárias caso ainda não existam."""

    # Abre uma conexão com o banco oficial
    conexao = sqlite3.connect(CAMINHO_BANCO)

    # Cria o cursor responsável pelos comandos SQL
    cursor = conexao.cursor()

    # Cria a tabela de botões caso ela ainda não exista
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS buttons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            acao TEXT NOT NULL
        )
        """
    )

    # Confirma a criação da tabela
    conexao.commit()

    # Fecha a conexão
    conexao.close()