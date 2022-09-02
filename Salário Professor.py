aulas = float(input ("Insira o número de aulas ao mês:"))
valor_aula = float(input("Insira o valor de cada aula:"))
salario_bruto = aulas*valor_aula
inss = salario_bruto*0.08
salario_liquido = salario_bruto - inss
print (f"O valor do salário líquido é {salario_liquido:.1f}.")
