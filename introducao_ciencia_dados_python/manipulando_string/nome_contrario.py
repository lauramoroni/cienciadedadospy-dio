# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = str(input("Informe o seu nome: "))

nome = nome.upper()

nome_invertido = nome[::-1]

print(f"O seu nome invertido é {nome_invertido}")