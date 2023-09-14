contatos = {
    "laura@gmail.com": {"nome": "laura", "idade": 18, "telefone": "4002-8922"},
    "maria@gmail.com": {"nome": "maria", "idade": 22, "telefone": "9924-3212"},
    "felipe@gmail.com": {"nome": "felipe", "idade": 28, "telefone": "9912-4109"}
}

for chave in contatos:
    print(chave, contatos[chave])
    print("=" * 75)
    
for chave, valor in contatos.items():
    print(chave,valor)