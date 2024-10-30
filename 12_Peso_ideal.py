#   Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#   usando a seguinte fórmula:
altura_usuario = float(input('Olá! Informe sua altura para que possamos calcular e obter o seu peso ideal: '))
formula_peso = (72.7 * altura_usuario) - 58
print(f'A sua altura é de {altura_usuario} cm e então seu peso idela será de {formula_peso} Kilos!')