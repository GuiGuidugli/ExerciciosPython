tamanho_arquivo = float(input('Insira o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade do link em MB/s: '))
tempo_download = (tamanho_arquivo/velocidade)/60
print(f'O tempo aproximado para download será {tempo_download:.2f} minuto(s).')
