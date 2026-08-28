import sqlite3 

conexao = sqlite3.connect("deck.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM buttons")

dados = cursor.fetchall()

print("botoes cadastrados")

for registro in dados:
    print("ID:", registro[0])
    print("NOME:", registro[1])
    print("TIPO:", registro[2])
    print("AÇÃO:", registro[3])    

conexao.close()