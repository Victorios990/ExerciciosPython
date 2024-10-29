#   Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       O produto do dobro do primeiro com metade do segundo .
#       A soma do triplo do primeiro com o terceiro.
#       O terceiro elevado ao cubo.
numero1_inteiro = int(input('Informe um numero inteiro: '))
numero2_inteiro = int(input('informe outro numero inteiro: '))
numero3_real = float(input('Informe um numero de valor real: '))
calculo1 = (numero1_inteiro * 2) + (numero2_inteiro / 2)
calculo2 = (numero1_inteiro * 3) + numero3_real
calculo3 = numero3_real ** 3
print(calculo1)
print(calculo2)
print(f'{calculo3:.2f}')