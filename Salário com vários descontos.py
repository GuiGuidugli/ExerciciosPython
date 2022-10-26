import math

inss = 0.08
ir = 0.11
sindicato = 0.05

valor_hora = float(input('Insira o valor da sua hora trabalhada: '))
numero_horas = float(input('Insira a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora*numero_horas
desconto_inss = inss*salario_bruto
desconto_sindicato = sindicato*salario_bruto
salario_liquido = salario_bruto-desconto_inss-desconto_sindicato

print (f'O valor do seu salário bruto é {salario_bruto}. Com o desconto de {desconto_inss:.2f} reais do INSS e {desconto_sindicato:.2f} reais do sindicato, o salário líquido equivale a {salario_liquido:.2f}.')