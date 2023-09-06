# lista os valores dentro do []
frutas = ["maça", "uva", "limão", "banana"]
frutas[0] # "maça"
frutas[2] # "limão"
frutas[-3] # "uva"
frutas[1] # "banana"

# lista as letras separadas
letras = list("python")
print(letras)

# lista números até 10 (sem incluir o 10)
numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420, 2015, "São Paulo"]
print(carro)

# lista aninhada
matriz = [
		[1, "a", 2]
    ["b", 3, 4]
		[6, 5, "c"]
]
matriz[0] # 1, "a", 2
matriz[0, 2] # 6
matriz [-1, -1] # "c"

# fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # inicia no índice dois -> t, h, o, n
lista[:2] # vai até o índice 2 (sem incluí-lo) -> p, y
lista[1:3] # y, t
lista[0:3:2] # inicia no 0, vai até o 3 (sem incluí-lo) e pula 2 -> p, t
lista[::-1] # fica invertido -> n, o, h, t, y, p