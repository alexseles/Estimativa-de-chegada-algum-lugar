partida = int(input("digite o horário de partida (hours): "))
mins = int(input("digite os minutos (minutes): "))
distancia = int(input("digite a distância a percorrer(km): "))
velocidade = int(input("digite a velocidade média (km): "))

dura = ((distancia/velocidade)*60)
mins = mins + dura # find a total of all minutes
partida = partida + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
partida = partida % 24 # correct hours to fall in the (0..23) range

print (" a estimativa de chegada será ás {:.0f}:{:.0f}h".format (partida, mins))
