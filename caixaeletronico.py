#defini uma variavel para o numero e depois inseri em divisoes pelos valores decrescentes das cedulas onde a divisao seguinte seria feita com base no resto  da divisao anterior. 

numero = int(input('Qual valor deseja sacar, sao permitidos apenas valores entre 10 e 600 reais!! '))
cem = int(numero / 100)
numero = numero % 100
    
cinquenta = int(numero/50)
numero = numero % 50

dez = int(numero/10)
numero = numero % 10

cinco = int(numero/5)
numero = numero % 5

um = numero
    
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)