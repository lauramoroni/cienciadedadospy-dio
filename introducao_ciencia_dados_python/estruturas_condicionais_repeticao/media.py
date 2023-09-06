# Faça um programa que leia a nota das três provas de um aluno e calcule a sua média. Se a média for maior ou igual a 7, exiba na tela que ele foi aprovado. Se for entre 4 e 7, recuperação; senão, reprovado. 

nota1 = float(input("informe o valor da primeira nota: "))
nota2 = float(input("informe o valor da segunda nota: "))
nota3 = float(input("informe o valor da terceira nota: "))

media = (nota1+nota2+nota3)/3
print(media)

if media>=7 :
    print("STATUS: APROVADO")
elif media<7 and media>4 :
    print("STATUS: RECUPERAÇÃO")
else :
    print("REPROVADO")