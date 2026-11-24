peso = float(input("Digite o seu peso (em kilos kg): "))

altura = float(input("Digite a sua altura (Metros): "))

imc = peso / (altura ** 2)

print(f"Seu imc é: {imc:.2f}")

match imc:
    case n if n < 17:
        print("Muito abaixo do peso")
    case n if n >= 17 and n < 18.5:
        print("Abaixo do peso")
    case n if n >= 18.5 and n < 25:
        print("Peso normal")
    case n if n >= 25 and n < 30:
        print("Acima do peso")
    case n if n >= 30 and n < 35:
        print("Obesidade grau I")
    case n if n >= 35 and n < 40:
        print("Obesidade grau II")
    case n if n > 40:
        print("Obesidade grau III")
