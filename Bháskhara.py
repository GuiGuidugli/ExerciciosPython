import  math

a = float(input('Digite o valor de A:\n\r'))
b = float(input('Digite o valor de B:\n\r'))
c = float(input('Digite o valor de C:\n\r'))

if b == 0:
    print ('A equação não é de segundo grau.')
else:
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print ('A equação não possui raízes reais.')
    elif delta == 0:
        x = -b/2*a
        print (f'A raíz real da equação é {x}.')
    else: 
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print (f'As raízes reais da equação são {x1} e {x2}.')
    