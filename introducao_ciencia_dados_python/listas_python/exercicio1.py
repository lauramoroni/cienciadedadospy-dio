lista_original = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = [numero for numero in lista_original if numero%2==0]
impares = [numero for numero in lista_original if numero%2==1]
multiplos = [numero for numero in lista_original if numero%2==0 and numero%3==0 and numero%4==0]


print(lista_original[1:10])
print(lista_original[8:14])
print(pares)
print(impares)
print(multiplos)
print(lista_original[::-1])

soma = 0

for i in range(10,16):
    soma += i
for i in range(3,10):
    print(soma/i)
