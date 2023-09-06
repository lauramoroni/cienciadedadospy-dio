# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input("Informe o valor do produto: "))
desconto = float(input("Informe o desconto adquirido (em %): "))

preco_final = preco-(preco*desconto/100)

print("O preço final do produto que custa {} é {}".format(preco, preco_final))