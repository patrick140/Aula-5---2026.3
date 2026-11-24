print("Digite 'ajuda' para ver os comandos.")

comando = input("Digite o comando: ")

match comando:
    case "oi":
        print("Ola, como posso lhe ajudar?")
    case "tchau":
        print("Ate mais!")
    case "ajuda":
        print("Os comandos: 'oi', 'tchau', 'ajuda'.")
    case _:
        print("Comando invalido.")