# inseri uma variavel para peso e depois com a função if comparei ao valor do excesso, caso seja maior que o excesso o valor a mais é multiplicado por 4 para calcular a multa.

print("/tJoão Papo-de-Pescador/n")

peso = float(input("Peso: "))
excesso = 0
multa = 0

if peso <= 50:
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)
else:
    excesso = peso - 50
    multa = excesso * 4

    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)
