n_nota1 = float(input('Digite a primeira nota:\n\r'))
n_nota2 = float(input('Digite a segunda nota:\n\r'))
conceito = ''
media = (n_nota1 + n_nota2)/2

if media >= 9:
    conceito = 'A'
    print ('Aprovado')
elif media < 9 and media >= 7.5:
    conceito = 'B'
    print ('Aprovado')
elif media < 7.5 and media >= 6.0:
    conceito = 'C'
    print ('Aprovado')
elif media < 6.0 and media >= 4.0:
    conceito = 'D'
    print ('Reprovado')
elif media < 4.0:
    conceito = 'E'
    print ('Reprovado')
else: 
    print ('Digite um valor válido!')

print (f'A sua primeira nota foi {n_nota1}, sua segunda nota foi {n_nota2} e a sua média foi {media}. Você se encaixou no conceito {conceito}.')