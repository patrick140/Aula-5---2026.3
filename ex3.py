peso_peixe = float(input("Digite o peso do peixe (somente o peso): "))

if peso_peixe > 100:
    valor_excedido = peso_peixe - 100
    multa = valor_excedido * 4.00
    print(f"O peso gerou a multa de: R$ {multa:.2f}")
else:
    print("Peso não gerou multa")