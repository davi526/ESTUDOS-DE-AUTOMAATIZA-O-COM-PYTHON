# ui/home_page.py

import customtkinter as ctk

from database.database_manager import Database
from services.action_executor import executar_acao


class HomePage:

    def __init__(self):

        self.database = Database()

        self.app = ctk.CTk()

        self.app.title("Python Deck")

        self.app.geometry("1200x700")

        self.criar_componentes()

    def criar_componentes(self):

        self.titulo = ctk.CTkLabel(
            self.app,
            text="Python Deck"
        )

        self.titulo.pack()

        self.botao_novo = ctk.CTkButton(
            self.app,
            text="Novo Botão",
            command=self.abrir_formulario
        )

        self.botao_novo.pack()

        self.carregar_botoes()

    def carregar_botoes(self):

        dados = self.database.listar_botoes()

        for registro in dados:

            nome = registro[1]
            acao = registro[3]

            botao = ctk.CTkButton(
                self.app,
                text=nome,
                command=lambda a=acao: executar_acao(a)
            )

            botao.pack()

    def abrir_formulario(self):

        print("Abrir formulário")

    def run(self):

        self.app.mainloop()