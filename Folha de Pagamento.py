<<<<<<< HEAD
n_valor_hora = float(input('Digite o valor da sua hora trabalhada:\n\r'))
n_qtde_horas = int(input('Digite a quantidade de horas trabalhadas:\n\r'))
n_salario_bruto = n_valor_hora * n_qtde_horas
ir = 0

if n_salario_bruto <= 900:
    ir = 'zero'
    n_salario_ir = n_salario_bruto * 1
elif n_salario_bruto > 900 and n_salario_bruto <=1500:
    ir = 'cinco'
    n_salario_ir = n_salario_bruto * 0.95
elif n_salario_bruto > 1500 and n_salario_bruto <= 2500:
    ir = 'dez'
    n_salario_ir = n_salario_bruto * 0.90
elif n_salario_bruto > 2500:
    ir = 'vinte'
    n_salario_ir = n_salario_bruto * 0.80
else:
    print ('Digite um valor válido!')

n_fgts = n_salario_bruto * 0.11
n_desconto_sindicato = n_salario_bruto * 0.03
n_salario_liquido = (n_salario_ir - n_desconto_sindicato)

print (f'O valor do salário bruto era de {n_salario_bruto} reais e a porcentagem de desconto do imposto de renda foi de {ir} por cento. O valor do FGTS depositado foi de {n_fgts} reais e o desconto do sindicato foi de {n_desconto_sindicato} reais. O valor do salário líquido após descontos é de {n_salario_liquido} reais.')
=======
p_fgts = 0
n_ir = 0

n_horas_mes = int(input('Insira a quantidade de horas trabalhadas no mês:\n\r'))
n_valor_hora = float(input('Digite o valor da sua hora trabalhada:\n\r'))
n_salario_bruto = n_horas_mes * n_valor_hora

if n_salario_bruto <= 900:
    n_ir = 0
    n_salario_ir = n_salario_bruto
elif n_salario_bruto > 900 and n_salario_bruto <= 1500:
    n_ir = n_salario_bruto * 0.05
    n_salario_ir = n_salario_bruto - n_ir
elif n_salario_bruto > 1500 and n_salario_bruto <= 2500:
    n_ir = n_salario_bruto * 0.10
    n_salario_ir = n_salario_bruto - n_ir
else:
    n_ir = n_salario_bruto * 0.20
    n_salario_ir = n_salario_bruto - n_ir

n_desconto_sindicato = n_salario_bruto * 0.03
p_fgts = n_salario_bruto * 0.11

n_salario_liquido = n_salario_ir - n_desconto_sindicato

print (f'O valor do salário bruto é de {n_salario_bruto} reais, o valor do salário líquido é de {n_salario_liquido} reais. O desconto do imposto de renda corresponde a {n_ir} reais, e o desconto do sindicato corresponde a {n_desconto_sindicato} reais. O valor depositado no FGTS foi de {p_fgts} reais.')
>>>>>>> d2126827b9371ea01dce88e4a1d6904ed2c55935
