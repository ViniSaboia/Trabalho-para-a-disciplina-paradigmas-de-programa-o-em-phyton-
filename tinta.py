# inseri uma variável para tamanho, fiz um cálculo com a metragem dividida pela capacidade de cada lata e caso o resultado dessa divisão seja diferente de zero uma nova lata deve ser adicionada, para me dar a quantidade correta de latas e o valor da compra do total das latas.


tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0
latas = int(litros / 18.0)
if litros % 18 != 0:
    latas += 1

print('Voce deverá comprar', latas, 'latas.')
print('O valor total é:', latas * 80)
