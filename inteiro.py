#defini uma variavel para o numero, inseri numa divisao inteira por 1, caso retornasse um valor diferente do numero digitado, o numero seria decimal.

numero = float(input('Digite um numero qualquer :'))

if(numero // 1 == numero): 
    print('\nNúmero inteiro !')
else:
    print('\nNúmero Decimal !')