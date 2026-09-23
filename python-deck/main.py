# Importa a função responsável por preparar o banco de dados
from database.db import inicializar_banco

# Importa a classe responsável pela interface principal
from ui.home_page import HomePage


# Garante que o banco e a tabela buttons existam
# antes que a interface tente consultar os botões
inicializar_banco()

# Cria o objeto que representa a tela principal do Python Deck
app = HomePage()

# Inicia a interface gráfica e mantém a janela aberta
app.run()