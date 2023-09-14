novo_dicionario = {"a": 10, "b": 20, "c": 30}
print(novo_dicionario.keys())

#

contato = { "laura@gmail.com":
    {"nome": "Laura", "idade": 18, "telefone": "4002-8922"}
    }
contato.setdefault("primeiro nome", "Maria")
print(contato)

#

contato.update({"laura@gmail.com": {"nome": "Lau"}})
print(contato)

#

# contato["chave"] KeyError
contato.get("chave")
contato.get("telefone", {})

#
contatos = {
    "maria@gmail.com": {"nome": "Maria", "idade": 21, "cidade": "Natal"},
    "julia@gmail.com": {"nome": "Julia", "idade": 22, "cidade": "Boa Vista"},
    "pedro@gmail.com": {"nome": "Pedro", "idade": 28, "cidade": "Curitiba"} 
}
print(contatos.keys())
print(contatos.values())

#

resultado = "maria@gmail.com" in contatos 
print(resultado)
resultado = "paulo@gmail.com" in contatos
print(resultado)

#

del contatos["julia@gmail.com"]
del contatos["pedro@gmail.com"]["cidade"]
print(contatos)