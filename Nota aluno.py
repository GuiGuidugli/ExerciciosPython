nota1 = float(input("Digite a primeira nota do aluno:\n\r "))
nota2 = float(input("Digite a segunda nota do aluno:\n\r "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print ("Aluno aprovado!")
elif media == 10:
    print ("Aluno aprovado com distinção!")
else: print ("Aluno reprovado!")
