import customtkinter as ctk
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk


class AddButtonPage:
	"""Janela secundária responsável pelo cadastro de atalhos."""

	def __init__(
		self,
		janela_pai,
		database,
		callback_atualizacao
	):
		# Guarda o objeto que cuida do banco de dados
		self.database = database

		# Guarda a função que atualizará a grade da HomePage
		self.callback_atualizacao = callback_atualizacao

		# Cria uma janela secundária ligada à janela principal
		self.janela = ctk.CTkToplevel(janela_pai)

		# Configurações da janela
		self.janela.title("Adicionar atalho")
		self.janela.geometry("380x430")
		self.janela.resizable(False, False)

		# Mantém o formulário acima da janela principal
		self.janela.transient(janela_pai)

		# Impede interação com a HomePage enquanto o formulário está aberto
		self.janela.grab_set()

		# Coloca o foco nesta janela
		self.janela.focus_force()

		# Fecha corretamente quando o usuário clicar no X
		self.janela.protocol(
			"WM_DELETE_WINDOW",
			self.fechar
		)

		# Centraliza o formulário em relação à janela principal
		self.centralizar_janela(janela_pai)

		# Cria os componentes visuais
		self.criar_componentes()


	def centralizar_janela(self, janela_pai):
		"""Centraliza o formulário sobre a janela principal."""

		# Atualiza as informações geométricas das janelas
		janela_pai.update_idletasks()

		largura = 380
		altura = 430

		# Posição e tamanho da janela principal
		pai_x = janela_pai.winfo_x()
		pai_y = janela_pai.winfo_y()
		pai_largura = janela_pai.winfo_width()
		pai_altura = janela_pai.winfo_height()

		# Calcula o centro da janela principal
		posicao_x = pai_x + (pai_largura - largura) // 2
		posicao_y = pai_y + (pai_altura - altura) // 2

		# Impede coordenadas negativas
		posicao_x = max(0, posicao_x)
		posicao_y = max(0, posicao_y)

		# Aplica tamanho e posição
		self.janela.geometry(
			f"{largura}x{altura}+{posicao_x}+{posicao_y}"
		)


	def criar_componentes(self):
		"""Cria todos os componentes visuais do formulário."""

		# Título do formulário
		titulo = ctk.CTkLabel(
			self.janela,
			text="NOVO ATALHO",
			font=("Arial", 22, "bold")
		)

		titulo.pack(
			pady=(25, 18)
		)

		# Campo de nome
		self.entrada_nome = ctk.CTkEntry(
			self.janela,
			width=300,
			height=38,
			placeholder_text="Nome do atalho"
		)

		self.entrada_nome.pack(
			pady=8
		)

		# Seletor do tipo de ação
		self.seletor_tipo = ctk.CTkOptionMenu(
			self.janela,
			width=300,
			height=38,
			values=[
				"Aplicativo",
				"Site",
				"Jogo",
				"Pasta",
				"Arquivo"
			],
			command=self.atualizar_dica_acao
		)

		self.seletor_tipo.pack(
			pady=8
		)

		# Define o tipo inicial
		self.seletor_tipo.set("Aplicativo")

		# Campo do caminho, endereço ou comando
		self.entrada_acao = ctk.CTkEntry(
			self.janela,
			width=300,
			height=38,
			placeholder_text="Caminho do aplicativo"
		)

		self.entrada_acao.pack(
			pady=8
		)

		# Botão para selecionar um executável sem executá-lo
		self.botao_selecionar_exe = ctk.CTkButton(
			self.janela,
			text="Selecionar .exe",
			width=300,
			height=34,
			command=self.selecionar_executavel
		)

		self.botao_selecionar_exe.pack(
			pady=(0, 8)
		)
		self.atualizar_dica_acao("Aplicativo")

		# Mensagem de validação
		self.label_mensagem = ctk.CTkLabel(
			self.janela,
			text="",
			text_color="#ff6b6b",
			wraplength=300
		)

		self.label_mensagem.pack(
			pady=(8, 4)
		)

		# Frame inferior dos botões
		frame_acoes = ctk.CTkFrame(
			self.janela,
			fg_color="transparent"
		)

		frame_acoes.pack(
			pady=14
		)

		# Botão Salvar
		botao_salvar = ctk.CTkButton(
			frame_acoes,
			text="Salvar",
			width=135,
			height=38,
			command=self.salvar
		)

		botao_salvar.grid(
			row=0,
			column=0,
			padx=6
		)

		# Botão Cancelar
		botao_cancelar = ctk.CTkButton(
			frame_acoes,
			text="Cancelar",
			width=135,
			height=38,
			fg_color="#555555",
			hover_color="#666666",
			command=self.fechar
		)

		botao_cancelar.grid(
			row=0,
			column=1,
			padx=6
		)

		# Coloca o cursor diretamente no campo de nome
		self.entrada_nome.focus_set()

		# Permite salvar pressionando Enter
		self.janela.bind(
			"<Return>",
			lambda evento: self.salvar()
		)

		# Permite cancelar pressionando Escape
		self.janela.bind(
			"<Escape>",
			lambda evento: self.fechar()
		)


	def atualizar_dica_acao(self, tipo_selecionado):
		"""Atualiza a orientação do campo conforme o tipo escolhido."""

		dicas = {
			"Aplicativo": "Caminho do aplicativo ou executável",
			"Site": "Endereço do site, começando com http",
			"Jogo": "Caminho do executável do jogo",
			"Pasta": "Caminho completo da pasta",
			"Arquivo": "Caminho completo do arquivo"
		}

		# Limpa o campo para atualizar corretamente o placeholder
		self.entrada_acao.delete(0, ctk.END)

		self.entrada_acao.configure(
			placeholder_text=dicas.get(
				tipo_selecionado,
				"Digite a ação do atalho"
			)
		)

		if tipo_selecionado == "Aplicativo":
			self.botao_selecionar_exe.pack(
				pady=(0, 8)
			)
		else:
			self.botao_selecionar_exe.pack_forget()


	def selecionar_executavel(self):
		"""Seleciona um arquivo .exe e preenche o campo de ação."""
		caminho = filedialog.askopenfilename(
			title="Selecionar aplicativo",
			filetypes=[
				("Aplicativos do Windows", "*.exe"),
				("Todos os arquivos", "*.*")
			]
		)

		if caminho:
			self.entrada_acao.delete(0, ctk.END)
			self.entrada_acao.insert(0, caminho)


	def validar_dados(self, nome, tipo, acao):
		"""Valida os dados antes de salvar no banco."""

		if not nome:
			return "Informe o nome do atalho."

		if len(nome) > 24:
			return "O nome deve possuir no máximo 24 caracteres."

		if not acao:
			return "Informe o caminho ou endereço do atalho."

		if tipo == "Site":
			if not (
				acao.startswith("http://")
				or acao.startswith("https://")
			):
				return "O endereço do site deve começar com http:// ou https://."

		caminho = acao.strip().strip('"').strip()

		if caminho.lower().endswith(".exe"):
			executavel = Path(caminho)

			if not executavel.exists() or not executavel.is_file():
				return "O arquivo .exe informado não existe ou não é um arquivo válido."

		return None


	def salvar(self):
		"""Captura, valida e salva o novo atalho."""

		# Captura os valores informados pelo usuário
		nome = self.entrada_nome.get().strip()
		tipo = self.seletor_tipo.get()
		acao = self.entrada_acao.get().strip()

		# Valida os dados
		mensagem_erro = self.validar_dados(
			nome,
			tipo,
			acao
		)

		# Interrompe o cadastro caso exista algum erro
		if mensagem_erro:
			self.label_mensagem.configure(
				text=mensagem_erro,
				text_color="#ff6b6b"
			)
			return

		try:
			# Salva o atalho no SQLite
			self.database.inserir_botao(
				nome,
				tipo,
				acao
			)

			# Reconstrói a grade da HomePage
			self.callback_atualizacao()

			# Fecha o formulário
			self.fechar()

		except Exception as erro:
			# Exibe uma mensagem amigável na interface
			self.label_mensagem.configure(
				text=f"Não foi possível salvar: {erro}",
				text_color="#ff6b6b"
			)

			# Exibe informações completas no terminal
			print(
				"ERRO AO SALVAR ATALHO:",
				erro
			)


	def fechar(self):
		"""Libera a janela principal e fecha o formulário."""

		# Libera o bloqueio da janela principal
		try:
			self.janela.grab_release()
		except Exception:
			pass

		# Destrói a janela secundária
		self.janela.destroy()
