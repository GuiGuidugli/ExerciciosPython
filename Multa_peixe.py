peso = float(input('Insira o peso do peixe em quilogramas: '))
multa = 4*(peso-50)
excesso = (peso-50)  
if peso>50.0:
    print (f'Você será multado em {multa} reais, pois o peso excede o limite em {excesso} quilos.')
else:
    print ('Você não será multado com este peso.')