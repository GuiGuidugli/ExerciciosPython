continuar = 's'

while (continuar == 's'):
    n_dia_da_semana = int(input('Digite um número de 1 a 7:\n\r'))

    if n_dia_da_semana == 1:
        print ('Hoje é domingo.')
    elif n_dia_da_semana == 2:
        print ('Hoje é segunda.')
    elif n_dia_da_semana == 3:
        print ('Hoje é terça.')
    elif n_dia_da_semana == 4:
        print ('Hoje é quarta.')
    elif n_dia_da_semana == 5:
        print ('Hoje é quinta.')
    elif n_dia_da_semana == 6:
        print ('Hoje é sexta.')
    elif n_dia_da_semana == 7:
        print ('Hoje é sábado.')
    else:
        print ('Digite um valor válido!')

    continuar = input("Deseja continuar? (s/n)")