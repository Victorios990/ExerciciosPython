#   Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
print('###########  SISTEMA PARA CALCULO DE PESO COM BASE APENAS EM SUA ALTURA ###########')

genero = str(input('Por favor, para uma melhor interação, informe o seu genero: '))
altura = float(input('Por favor, informe sua altura: '))

formula_para_homens = (72.7 * altura) - 58
formula_para_mulheres = (62.1 * altura) - 44.7

while genero in genero:
    if genero == 'masculino':
        print(f'Com base na sua altura de {altura:.2f} cm, seu peso ideal é de {formula_para_homens:.2f} Kilos')
    elif genero == 'feminino':
        print(f'Com base na sua altura de {altura:.2f} cm, seu peso ideal é de {formula_para_mulheres:.2f} Kilos')
    else:
        print(f'Com base na sua altura de {altura:.2f} cm, seu peso ideal é para alguem com o gene masculino é de {formula_para_homens:.2f} Kilos')
        print(f'Com base na sua altura de {altura:.2f} cm, seu peso ideal é alguem com o gene feminino é de {formula_para_mulheres:.2f} Kilos')
    break