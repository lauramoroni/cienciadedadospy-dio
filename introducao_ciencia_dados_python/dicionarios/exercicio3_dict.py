#  Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário. 

pessoas = {
    "laura":{"nome": "Maria Laura", "idade": 18, "cpf": "123456789-12"},
    "lipe":{"nome": "Felipe Barboza", "idade": 7, "cpf": "987654321-98"},
    "liz":{"nome": "Liz Barboza", "idade": 3, "cpf": "28491792-08"},
    "paulo":{"nome": "Paulo Souza", "idade": 22, "cpf": "125871791-12"},
    "pedro":{"nome": "Pedro Silva", "idade": 28, "cpf":"098786342-16"}
}

menores_de_18 = {}

idades = [info["idade"] for info in pessoas.values()]

for chave, valor in pessoas.items():
    if valor["idade"]<18:
        menores_de_18[chave] = valor
        
for chave in menores_de_18.keys():
    del pessoas[chave]

print("pessoas menores de 18 anos")        
print(menores_de_18)
print("pessoas maiores de 18 anos")
print(pessoas)