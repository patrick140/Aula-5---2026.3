print("Digite os seguintes animais: ")
print("cachorro\n gato\n leão\n tigre\n")
animal = input("Digite o nome de um dos animais listados: ")

match animal:
    case "cachorro" | "gato" | "coelho":
        print("Este é um animal domesticado.")
    case "leão" | "tigre":
        print("Este é um animal selvagem!")
    case _:
        print("Animal invalido ou nome digitado incorretamente.")