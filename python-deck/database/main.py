from database_manager import Database

database = Database()


def definir_opcao():

    print("Escolha uma opção:")
    print("1. Listar botões")
    print("2. Inserir botão")
    print("3. Editar botão")
    print("4. Deletar botão")
    print("5. Sair")

    return input("Opção: ")

while True:

    opcao = definir_opcao()


    if opcao == "1":

        database.Listar_botoes()

    elif opcao == "2":

        nome = input("Digite o nome para o botão: ")

        tipo = input("Digite o tipo do botão: ")

        acao = input("Digite a ação do botão: ")

        database.inserir_botao(
            nome,
            tipo,
            acao
        )


    elif opcao == "3":

        id_botao = input("Digite o ID do botão que deseja editar: ")

        nome = input("Digite o novo nome para o botão: ")
        tipo = input("Digite o novo tipo do botão: ")
        acao = input("Digite a nova ação do botão: ")

        database.editar_botao(
            id_botao,
            nome,
            tipo,
            acao
        )

    elif opcao == "4":

        id_botao = input("Digite o ID do botão que deseja deletar: ")

        database.deletar_botao(id_botao)

    elif opcao == "5":
        
        print("Saindo do programa...")
        break
        
        

    else:

        print("Opção inválida. Tente novamente.")