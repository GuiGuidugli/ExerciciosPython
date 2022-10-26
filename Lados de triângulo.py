n_primeiro_lado = float(input('Digite o valor do primeiro lado:\n\r'))
n_segundo_lado = float(input('Digite o valor do segundo lado:\n\r'))
n_terceiro_lado = float(input('Digite o valor do terceiro lado:\n\r'))

if n_primeiro_lado + n_segundo_lado > n_terceiro_lado or n_segundo_lado + n_terceiro_lado > n_primeiro_lado or n_primeiro_lado + n_terceiro_lado > n_segundo_lado:
    if n_primeiro_lado == n_segundo_lado and n_segundo_lado == n_terceiro_lado:
        print ('O triângulo é equilátero.')
    elif n_primeiro_lado == n_segundo_lado or n_primeiro_lado == n_terceiro_lado or n_segundo_lado == n_terceiro_lado:
        print ('O triângulo é isósceles.')
    elif n_primeiro_lado != n_segundo_lado and n_segundo_lado != n_terceiro_lado:
        print ('O triângulo é escaleno.')
else:
    print ('O polígono não é um triângulo.')   
