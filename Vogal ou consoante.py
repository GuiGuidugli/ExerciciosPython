Valor = str(input("Digite uma letra: "))
if (Valor in ("a","e","i","o","u")): 
    print ("A letra é uma vogal.")
elif (Valor.isdigit()):
    print ("Insira um valor válido!")
else:
    print ("A letra é uma consoante.")
