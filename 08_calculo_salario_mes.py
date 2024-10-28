#   Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   Calcule e mostre o total do seu salário no referido mês.

print('Bem vindo ao PAGPYTHON, Sistema de calculo de salario')
valor_hora_trabalhada = float(input('Informe o valor que recebe por hora trabalhada: '))
hora_dia_trabalhada = int(input('Informe quantas horas trabalha por dia: '))
dias_trabalhados_mes = int(input('Quantos dias trabalhou no mes: '))
salario_do_mes = (valor_hora_trabalhada * hora_dia_trabalhada) * dias_trabalhados_mes
print(f'Nesse mês você trabalhou {dias_trabalhados_mes} dias, em cada dia realizou uma carga horaria de {hora_dia_trabalhada} horas,'
      f'o valor da sua hora é de {valor_hora_trabalhada}, com base nas informações anteriores seu salario será de R$ {salario_do_mes}')