from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk

from services.registry import get_action
from ui.add_button_page import AddButtonPage


class EditButtonPage(AddButtonPage):
	"""Janela para editar os dados de um botão existente."""

	def __init__(
		self,
		janela_pai,
		database,
		id_botao,
		nome_atual,
		tipo_atual,
		acao_atual,
		callback_atualizacao
	):
		self.id_botao = id_botao

		super().__init__(
			janela_pai=janela_pai,
			database=database,
			callback_atualizacao=callback_atualizacao
		)

		self.janela.title("Editar Botão")
		self.preencher_dados(
			nome_atual,
			tipo_atual,
			acao_atual
		)


	def preencher_dados(self, nome, tipo, acao):
		"""Preenche o formulário com os dados atuais do botão."""
		self.entrada_nome.insert(0, nome)
		self.seletor_tipo.set(tipo)
		self.atualizar_dica_acao(tipo)
		self.entrada_acao.insert(0, acao)


	def _remover_aspas_externas(self, valor):
		"""Remove apenas aspas que envolvem todo o caminho."""
		valor = valor.strip()

		if len(valor) >= 2 and valor[0] == valor[-1] == '"':
			return valor[1:-1].strip()

		return valor


	def validar_edicao(self, nome, tipo, acao):
		"""Valida os dados antes de atualizar o registro."""
		if not nome:
			return "Informe o nome do atalho."

		if len(nome) > 24:
			return "O nome deve possuir no máximo 24 caracteres."

		if not tipo:
			return "Informe o tipo do atalho."

		if not acao:
			return "Informe a ação do atalho."

		if tipo == "Site":
			if not acao.startswith(("http://", "https://")):
				return "O endereço do site deve começar com http:// ou https://."
			return None

		if tipo == "Aplicativo":
			if get_action(acao) is not None:
				return None

			caminho = self._remover_aspas_externas(acao)
			executavel = Path(caminho)

			if not executavel.exists() or not executavel.is_file():
				return "O arquivo .exe informado não existe ou não é válido."

			if executavel.suffix.lower() != ".exe":
				return "O aplicativo deve ser um arquivo com extensão .exe."

		return None


	def selecionar_executavel(self):
		"""Seleciona um .exe e preenche o campo sem executá-lo."""
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


	def salvar(self):
		"""Valida e salva as alterações no SQLite."""
		nome = self.entrada_nome.get().strip()
		tipo = self.seletor_tipo.get().strip()
		acao = self.entrada_acao.get().strip()

		mensagem_erro = self.validar_edicao(nome, tipo, acao)

		if mensagem_erro:
			messagebox.showerror("Dados inválidos", mensagem_erro)
			return

		if self.database.atualizar_botao(
			self.id_botao,
			nome,
			tipo,
			acao
		):
			messagebox.showinfo("Atalho atualizado", "Alterações salvas.")
			self.callback_atualizacao()
			self.fechar()
			return

		messagebox.showerror(
			"Erro ao salvar",
			"Não foi possível atualizar o atalho."
		)
