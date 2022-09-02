from re import M
sexo=str(input('Insira o seu sexo: '))
altura=float(input('Insira sua altura em centímetros: '))
if sexo=='M':
   peso_ideal_m=((72.7*altura/100))-58
   print(f'O seu peso ideal é {peso_ideal_m:.1f} quilos.')
else:
   peso_ideal_f=(62.1*(altura/100))-44.7
   print(f'O seu peso ideal é {peso_ideal_f:.1f} quilos.')