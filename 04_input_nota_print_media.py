#   Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Bem vindo ao sistema de notas da Escola CEF PYTHON!')
print('Entre com as notas bimestrais e logo a média final será informada!')
primeiro_bimestre = float(input('Média do primeiro bimestre: '))
segundo_bimestre = float(input('Média do segundo bimestre: '))
terceiro_bimestre = float(input('Média do terceiro bimestre: '))
quarto_bimestre = float(input('Media do quarto bimestre: '))
soma_media = primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre
media_final = soma_media / 5
print(f'O aluno ficou com uma média final {media_final}!')