#   Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#   pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
#   latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
#   arredonde os valores para cima, isto é, considere latas cheias.

import math

print('############# BEM VINDO AO PYTHON COLORS AND PAINTING #############')
print('#############        VAMOS AOS TRABALHOS!!!       #############')

metros2= float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
litros_lata = 18
preço_lata_18lts = 80
litro_galao = 3.6
preco_galao = 25
litros_necessarios = metros2 / 6

quantidade_latas = math.ceil(litros_necessarios / litros_lata)
gasto_latas = quantidade_latas * preço_lata_18lts
print(f'Apenas latas de 18 litros: {quantidade_latas} latas, preço de R$ {gasto_latas}.')

quantidade_galoes = math.ceil(litros_necessarios / litro_galao)
gasto_galão = quantidade_galoes * preco_galao
print(f'Apenas galoes de 3.6 litros: {quantidade_galoes}, preço de R$ {gasto_galão}.')

compra_segura = litros_necessarios * 1.1
quanti_compra_segura = compra_segura // litros_lata

litros_para_comprar_folga = compra_segura - (quanti_compra_segura * litros_lata)
quantidade_galoes_sobra = math.ceil(litros_para_comprar_folga / litro_galao)

custo_lata_galao = (quanti_compra_segura * preço_lata_18lts) + (quantidade_galoes_sobra * preco_galao)

print(f'Mistura de latas e galões, {quanti_compra_segura} latas, {quantidade_galoes_sobra} com o preço de R$ {custo_lata_galao}.')