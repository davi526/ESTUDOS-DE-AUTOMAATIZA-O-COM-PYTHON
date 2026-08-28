# Importa a biblioteca SQLite
import sqlite3

# Abre conexão com o banco
conexao = sqlite3.connect("deck.db")

# Cria o cursor responsável por executar SQL
cursor = conexao.cursor()

# Insere um novo registro na tabela buttons
cursor.execute(
    """
    INSERT INTO buttons (nome, tipo, acao)
    VALUES (?, ?, ?)
    """,
    ("Chrome", "app", "chrome.exe")
)

# Salva as alterações
conexao.commit()

# Fecha a conexão
conexao.close()

# Apenas para confirmar que o programa terminou
print("Botão cadastrado com sucesso!")