import webbrowser


def executar_acao(acao):
    """
    Executa uma ação cadastrada no Python Deck.

    Nesta primeira versão serão tratados apenas sites.
    """

    print(f"Executando: {acao}")

    webbrowser.open(acao)