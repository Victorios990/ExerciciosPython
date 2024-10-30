#   João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#   Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#   deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#   calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#   Imprima os dados do programa com as mensagens adequadas.

print('######### CONTROLE NACIONAL DE PESAGEM DE PEIXES - CNPP  ############')
print('######### CONTROLE DE PESCA DA CIDADE DE SÃO PAULO = CPCSP  ############')

peso_total_peixe = float(input('informe o peso total dos peixes obtidos: '))
peso_limite_regulamento_kilo = 50
peso_excedente_X_multa = 4 * (peso_total_peixe - peso_limite_regulamento_kilo)
#   Multa de R$ 4,00 por quilo excedente

while peso_total_peixe > peso_limite_regulamento_kilo:
    if peso_total_peixe > peso_limite_regulamento_kilo:
        print(f'Você ultrapassou o limite estabelecido de {peso_limite_regulamento_kilo} kilos!, com uma multa de R$ '
              f'4,00 por cada kilo ultrapassado, o valor total da multa é de {peso_excedente_X_multa:.2f}')
#    elif peso_total_peixe <= peso_limite_regulamento_kilo:
#        print(f'O peso de {peso_total_peixe} kilos está dentro do regulamento.')
    else:
        print(f'O peso de {peso_total_peixe} kilos está dentro do regulamento.')