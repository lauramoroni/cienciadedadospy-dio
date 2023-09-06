# Escreva um programa que leia um valor em metros e o exiba convertido em kilometros, centimetros e milímetros.

metro = float(input("Informe o valor em metros: "))
print("[1] Kilometros (km)")
print("[2] Centímetros (cm)")
print("[3] Milímetros (mm)")

escolha = int(input("Escolha para qual deseja converter: "))

if escolha==1 :
    resultado = metro/1000
    print("{}m representa {}km".format(metro, resultado))
elif escolha==2 :
    resultado = metro*100
    print("{}m representa {}cm".format(metro, resultado))
elif escolha==3 :
    resultado = metro*1000
    print("{}m representa {}mm".format(metro, resultado))
else :
    print("Resposta inválida!")
    