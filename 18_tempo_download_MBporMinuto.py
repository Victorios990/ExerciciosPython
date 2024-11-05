#   Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
#   (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
arquivo_MB = float(input('Informe o tamanho do arquivo para download: '))
velocidade_internet = int(input('Informe a velocidade de sua internet: '))
tempo_downlaod = arquivo_MB / velocidade_internet
minuto = tempo_downlaod * 60
print(f'O tempo para o seu download é de {minuto} minutos!')