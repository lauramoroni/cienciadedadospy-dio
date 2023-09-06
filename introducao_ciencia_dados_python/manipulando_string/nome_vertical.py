# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical

nome = str(input("Informe o seu nome: "))
nome = nome.upper()
aux = 0

while aux<len(nome) :
    print((nome[aux]))
    aux = aux+1