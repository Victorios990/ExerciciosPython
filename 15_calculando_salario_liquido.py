import math

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print("#################    CALCULADORA PARA FINS DE PAGAMENTO - VALOR LIQUIDO  #################")
valor_hora = float(input('Insira o valor em R$ recebido por hora: '))
#dias_trabalhados = int(input('Informe quantos dias trabalhou nesse mês: '))
horas_trabalhadas = float(input('Informe o numero de horas trabalhadas no mês: '))
salario_bruto = valor_hora * horas_trabalhadas
print(f'O seu salario bruto é R$ {salario_bruto:.2f}')
desconto_inss = salario_bruto * (8 / 100)
imposto_de_renda = salario_bruto * (11 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - imposto_de_renda - desconto_inss - sindicato
print(f'O valor pago ao inss é de R$ {desconto_inss:.2f}')
print(f'O valor pago de imposto de renda é de R$ {imposto_de_renda:.2f}.')
print(f'O valor pago ao sindicato é de R$ {sindicato:.2f}.')
print(f'Salario liquido recebido é de R$ {salario_liquido:.2f}')