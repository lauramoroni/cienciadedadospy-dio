# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Informe o seu salário: "))
aumento = float(input("Informe o aumento (%): "))

novo_salario = salario+(salario*aumento/100)


print("Um aumento de {} % no salário resulta em R${}".format(aumento, novo_salario))