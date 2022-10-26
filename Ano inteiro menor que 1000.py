numero = float(input('Digite um número menor que 1000:'))

if numero > 1000:
    float(input('Digite um número menor que 1000:'))
    
else:
    centena = numero // 100
    dezena = (numero - (centena * 100)) // 10
    unidade = (numero - (centena * 100 + (dezena * 10)))
    if centena > 1:
        


print (f'O número possui ')