# Importa o CustomTkinter
import customtkinter as ctk

# Importa a classe responsável pelo banco
from database.database_manager import Database
from ui.add_button_page import AddButtonPage
from ui.edit_button_page import EditButtonPage
from services.action_executor import executar_acao


class HomePage:

    def __init__(self):

        # Cria o objeto responsável pelo banco
        self.database = Database()

        # Cria a janela principal
        self.app = ctk.CTk()
        self.formulario_adicao = None
        self.formulario_edicao = None

        # Define o título da janela
        self.app.title("Python Deck")

        # Define o tamanho inicial
        self.posicionar_janela()

        # Define uma largura e altura mínimas
        self.app.minsize(400, 700)

        # Cria os componentes visuais
        self.criar_componentes()


    def posicionar_janela(self):

        # Define o tamanho do Python Deck
        largura_janela = 400
        altura_janela = 700

        # Descobre a largura total da tela
        largura_tela = self.app.winfo_screenwidth()

        # Descobre a altura total da tela
        altura_tela = self.app.winfo_screenheight()

        # Define uma margem em relação às bordas
        margem_direita = 20
        margem_inferior = 60

        # Calcula a posição horizontal
        posicao_x = largura_tela - largura_janela - margem_direita

        # Calcula a posição vertical
        posicao_y = altura_tela - altura_janela - margem_inferior

        # Aplica tamanho e posição
        self.app.geometry(
            f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}"
        )


    def criar_componentes(self):

        # Cria o título principal
        self.titulo = ctk.CTkLabel(
            self.app,
            text="PYTHON DECK",
            font=("Arial", 28, "bold")
        )

        # Posiciona o título
        self.titulo.pack(pady=(20, 10))

        # Cria uma área exclusiva para os atalhos
        self.frame_botoes = ctk.CTkFrame(
            self.app
        )

        # Faz a área preencher o espaço disponível
        self.frame_botoes.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # Cria o botão para adicionar novos atalhos
        self.botao_novo = ctk.CTkButton(
            self.app,
            text="+ Novo Botão",
            command=self.abrir_formulario
        )

        # Posiciona o botão na parte inferior
        self.botao_novo.pack(pady=(10, 20))

        # Carrega os registros do banco
        self.carregar_botoes()


    def carregar_botoes(self):

        # Busca no banco todos os atalhos já cadastrados
        dados = self.database.listar_botoes()

        # Exibe os registros no terminal para facilitar a depuração
        print("DADOS RECEBIDOS NA HOMEPAGE:", dados)

        # Faz as quatro colunas dividirem igualmente o espaço do frame
        for coluna in range(4):
            self.frame_botoes.grid_columnconfigure(
                coluna,
                weight=1
            )

        # Cria exatamente 12 posições na grade
        for indice in range(12):

            # Cria uma nova linha a cada quatro atalhos
            linha = indice // 4

            # Distribui os atalhos entre as colunas 0, 1, 2 e 3
            coluna = indice % 4

            # Verifica se existe um registro para esta posição
            if indice < len(dados):

                # Recupera o registro correspondente
                registro = dados[indice]

                # Extrai as informações do registro
                id_botao = registro[0]
                nome = registro[1]
                tipo = registro[2]
                acao = registro[3]

                # Cria o botão de um atalho cadastrado
                botao = ctk.CTkButton(
                    self.frame_botoes,
                    text=nome,
                    width=65,
                    height=65,
                    corner_radius=12,
                    command=lambda valor=acao: executar_acao(valor)
                )

                botao.bind(
                    "<Button-3>",
                    lambda evento,
                           id_atual=id_botao,
                           nome_atual=nome,
                           tipo_atual=tipo,
                           acao_atual=acao: self.abrir_editor(
                               id_atual,
                               nome_atual,
                               tipo_atual,
                               acao_atual
                           )
                )

            else:

                # Cria uma posição livre para adicionar um novo atalho
                botao = ctk.CTkButton(
                    self.frame_botoes,
                    text="+",
                    width=65,
                    height=65,
                    corner_radius=12,
                    font=("Arial", 24, "bold"),
                    fg_color="#404040",
                    hover_color="#505050",
                    command=self.abrir_formulario
                )

            # Posiciona o botão na grade
            botao.grid(
                row=linha,
                column=coluna,
                padx=8,
                pady=10
            )


    def abrir_formulario(self):

        # Se já existe um formulário aberto, apenas coloca o foco nele
        if (
            self.formulario_adicao is not None
            and self.formulario_adicao.janela.winfo_exists()
        ):
            self.formulario_adicao.janela.focus_force()
            return

        # Cria a janela de cadastro
        self.formulario_adicao = AddButtonPage(
            janela_pai=self.app,
            database=self.database,
            callback_atualizacao=self.atualizar_grade
        )

        # Detecta quando o formulário for destruído
        self.formulario_adicao.janela.bind(
            "<Destroy>",
            self.ao_fechar_formulario
        )


    def ao_fechar_formulario(self, evento):

        # Confirma que o evento pertence à janela principal do formulário
        if (
            self.formulario_adicao is not None
            and evento.widget == self.formulario_adicao.janela
        ):
            self.formulario_adicao = None


    def abrir_editor(self, id_botao, nome, tipo, acao):
        """Abre o editor do botão selecionado com o botão direito."""
        if (
            self.formulario_edicao is not None
            and self.formulario_edicao.janela.winfo_exists()
        ):
            self.formulario_edicao.janela.focus_force()
            return "break"

        self.formulario_edicao = EditButtonPage(
            janela_pai=self.app,
            database=self.database,
            id_botao=id_botao,
            nome_atual=nome,
            tipo_atual=tipo,
            acao_atual=acao,
            callback_atualizacao=self.atualizar_grade
        )

        self.formulario_edicao.janela.bind(
            "<Destroy>",
            self.ao_fechar_editor
        )

        return "break"


    def ao_fechar_editor(self, evento):
        """Remove a referência do editor quando a janela é fechada."""
        if (
            self.formulario_edicao is not None
            and evento.widget == self.formulario_edicao.janela
        ):
            self.formulario_edicao = None


    def atualizar_grade(self):

        # Remove todos os atalhos visuais atuais
        for widget in self.frame_botoes.winfo_children():
            widget.destroy()

        # Recria a grade utilizando os dados atualizados do SQLite
        self.carregar_botoes()


    def run(self):

        # Mantém a interface aberta
        self.app.mainloop()
