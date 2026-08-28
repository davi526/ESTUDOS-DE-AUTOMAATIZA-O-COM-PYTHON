# Importa a biblioteca SQLite que já vem com o Python
import sqlite3

# Cria uma conexão com o banco de dados
# Se o arquivo não existir, ele será criado
conexao = sqlite3.connect("deck.db")

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Executa o comando SQL para criar a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS buttons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    acao TEXT NOT NULL
)
""")

# Salva as alterações feitas no banco
conexao.commit()

# Fecha a conexão com o banco
conexao.close()