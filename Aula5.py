print("1 - Cadastrar 2- Listar 3 - Sair")
opcao = int(input("Digite o numero da opção: "))

match opcao:
    case n if n == 1:
        print("Você escolheu cadastrar!")
    case 2:
        print("Você escolheu listar!")
    case 3:
        print("Você escolheu sair!")
    case _:
        print("Opção invalida!")