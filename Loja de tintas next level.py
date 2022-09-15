import math
area= float(input('Insira o tamanho da área a ser pintada em metros quadrados: '))
litros = area/6
latas = litros/18
galoes = litros/3.6
latas_arredondada = math.ceil(latas)
galoes_arredondado = math.ceil(galoes)
preco_latas = latas_arredondada*80
preco_galoes = galoes_arredondado*25
print(f'A quantidade de litros a ser comprada é {litros:.1f}. Caso você queira comprar apenas latas, será necessário comprar {latas_arredondada} lata(s), pelo preço de {preco_latas} reais. Caso você queira comprar apenas galões, será necessário comprar {galoes_arredondado} galão(ões), pelo preço de {preco_galoes} reais. Caso você queria misturar ambos, será necessário comprar ')
