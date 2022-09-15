import math
Area = int(input("Qual a medida da area a ser pintada em metros quadrados? "))
AreaStr = str(Area)
newArea = Area * 1.1 #Esta fórmula define 10% de folga para a área recebida#
precoLata = 80
precoGalao = 25
coberturaLata = 18*6
coberturaGalao = 3.6*6 #Este e o de cima mostram a área que cada recipiente cobre#

if (newArea <= coberturaLata): print (f'Será necessário apenas uma lata de tinta, ao preço de {precoLata} reais.') #Define apenas uma lata se a área coberta requisitar apenas uma lata#
else:
     latasNecessarias = newArea // coberturaLata #Define a qtde de latas necessárias para cobrir a área recebida#
     galoesNecessarios = (newArea - (latasNecessarias * 108)) / 21.6 #Define a qtde de galões necessários depois de compensado o quanto foi coberto pelas latas#
     if (galoesNecessarios % 1 == 0):
         galoesNecessarios = galoesNecessarios
     else: (galoesNecessarios // 1) + 1  

totalLatas = latasNecessarias * precoLata
totalGaloes = galoesNecessarios * precoGalao
total = totalLatas + totalGaloes

print (f'Serão necessárias {latasNecessarias} lata(s) de tinta e {math.ceil(galoesNecessarios)} galão(ões) de tinta para cobrir a área a ser pintada; e o preço total é {total:.1f}')

