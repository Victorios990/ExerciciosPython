#   Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#   C = 5 * ((F-32) / 9).

graus_Fahrenheit = float(input("Informe a temperatura em graus Fahrenheit que sera convertida em Celsius: "))
conversao_celsius = 5 * ((graus_Fahrenheit-32) / 9)
print(f'A temperatura de {graus_Fahrenheit} °F é equivalente a {conversao_celsius:.2f} °C')
