# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input("Primeira frase: ")
string2 = input("Segunda frase: ")

print(f"String 1: {string1}")
print(f"Tamanho da String 1: {len(string1)}")
print(f"String 2: {string2}")
print(f"Tamanho da String 1: {len(string2)}")

if len(string1)==len(string2) :
    print("As duas strings são de tamanhos iguais.")
else :
    print("As duas strings são de tamanhos diferentes.")

if string1==string2 :
    print("As duas strings possuem conteúdo igual.")
else :
    print("As duas strings possuem conteúdo diferente.")