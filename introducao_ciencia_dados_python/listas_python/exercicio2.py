# Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

numeros = []

for i in range(5):
    numero = int(input(f"Digite o número de índice {i}: "))
    numeros.append(numero)
print(numeros)

for i, numero in enumerate(numeros):
    print(f"O número {numero} está na posição {i}")
    
# Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros2 = []

for n in range (10):
    numero2 = int(input("infomre os numeros: "))
    numeros2.append(numero2)
    print(numeros2[::-1])