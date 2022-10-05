n_porcentagem = ''
n_salario_original = float(input('Digite o valor do salário:\n\r '))
n_aumento = 0
n_salario_aumento = 0

if n_salario_original <= 280:
    n_porcentagem = '20%'
    n_salario_aumento = n_salario_original * 1.20
    n_aumento = n_salario_aumento - n_salario_original

elif n_salario_original > 280 and n_salario_original <= 700:
    n_porcentagem = '15%'
    n_salario_aumento = n_salario_original * 1.15
    n_aumento = n_salario_aumento - n_salario_original

elif n_salario_original > 700 and n_salario_original < 1500:
    n_porcentagem = '5%'
    n_salario_aumento = n_salario_original * 1.05
    n_aumento = n_salario_aumento - n_salario_original

print (f'O salário original era {n_salario_original}, a porcentagem do aumento foi de {n_porcentagem}, o valor do aumento foi de {n_aumento} e o valor do novo salário é de {n_salario_aumento}.')  