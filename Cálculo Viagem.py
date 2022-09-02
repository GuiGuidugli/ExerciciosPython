tempo = float (input ("Insira o tempo gasto na viagem:"))
velocidade_med = float (input ("Insira a velocidade média da viagem:"))
distancia = tempo * velocidade_med
litros_usados = distancia/12 
print ({f"A velocidade média foi {velocidade_med:.1f} km/h, o tempo da viagem foi {tempo:.1f}h, a distância percorrida foi {distancia:.1f} quilômetros e foram usados {litros_usados:.1f} litros na viagem."})