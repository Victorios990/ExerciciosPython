#   Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_celsius = int(input('Informe a temperatura em °C para que possamos converter em Fahrenheit: '))
conversao_para_fahrenheit = (temperatura_celsius * 9 / 5) + 32
print(f'O valor informado de {temperatura_celsius} °C é equivalente a {conversao_para_fahrenheit} °F')
