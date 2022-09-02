import math
area = float(input('Insira a área do cômodo em metros quadrados: '))
litros_tinta = area/3
total_latas = litros_tinta/18
total_latas_arredondado = math.ceil(total_latas) 
preco = total_latas_arredondado*80
print(f'Será necessário comprar {total_latas_arredondado} lata(s) de tinta e o preço total é {preco:.2f} reais.')
