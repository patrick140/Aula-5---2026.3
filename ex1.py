nota = float(input("Digite a nota do aluno: "))

match nota:
        case n if n >= 9 and n <= 10:
            print("Conceito A - Excelente")
        case n if n >=  7 and n < 9:
            print("Conceito B - Bom")
        case n if n >= 5 and n < 7:
            print("Conceito C - regular")
        case n if n < 5 and n >= 0:
            print("Conceito D - reprovado")
        case _:
            print("Nota invalida.")