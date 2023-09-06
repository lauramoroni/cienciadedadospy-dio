# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Informe a distância em Km: "))
velocidade = int(input("Informe a velocidade em Km/h: "))
horas = distancia/velocidade

if horas >= 1 : 
    print("O tempo estimado é de {} horas".format(horas))
else :
    minutos = horas*60
    print("O tempo estimado é de {} minutos e {} segundos".format(minutos))