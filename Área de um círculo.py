from cmath import pi
import math
unidade = str (input ('Insira a unidade de medida do raio: '))
raio = float (input ('Insira o valor do raio do círculo: '))
area_circulo = math.pi*raio*raio
print (f'A área do círculo é {area_circulo:.1f} {unidade}')
