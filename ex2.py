mes = int(input("Digite um numero de 1-12 correspondente a um mês: "))
#utiliza jogo da velha para comentarios
match mes:
    case 1: 
        print("janeiro.")
    case 2: 
        print("Fevereiro.")
    case 3:
        print("Março.")
    case 4:
        print("Abril.")
    case 5:
        print("Maio.")
    case 6:
        print("Junho.")
    case 7:
        print("Julho.")
    case 8:
        print("Agosto.")
    case 9:
        print("Setembro.")
    case 10:
        print("Outubro.")
    case 11:
        print("Novembro.")
    case 12:
        print("Dezembro.")
    case _:
        print("Mês invalido!")
