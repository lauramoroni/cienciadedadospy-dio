# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado. (NÃO CONSEGUI)
import random

palavras = ["Cachorro", "Gato", "Rato", "Passaro", "Macaco", "Cavalo", "Vaca", "Porco", "Guaxinim", "Elefante", "Crocodilo"]

# escolher aleatoriamente uma palavra dessa lista

palavra_secreta = (random.choice(palavras))
tamanho_palavra = len(palavra_secreta)

# Inicializar a variável que conterá a palavra oculta
palavra_oculta = ""
for letra in palavra_secreta:
    if letra.isalpha():
        palavra_oculta += "_ "
    else:
        palavra_oculta += letra

# Exibir a palavra oculta na tela
print(palavra_oculta)

MAXIMO_TENTATIVAS = 6
tentativas = 0

while tentativas<MAXIMO_TENTATIVAS :
    letra = str(input("Informe uma letra: ").upper())
    if letra in palavra_oculta :
        nova_palavra_oculta = ""
        for aux in range(tamanho_palavra):
            if palavra_oculta[aux] == letra:
                nova_palavra_oculta += letra
            else:
                nova_palavra_oculta += palavra_oculta[aux]
        palavra_oculta = nova_palavra_oculta
    else :
        tentativas += 1
        print(f"A letra {letra} não está na palavra. Você ainda tem {MAXIMO_TENTATIVAS-tentativas} tentativas restantes.")
    print("".join(list(palavra_oculta)))
    
    if palavra_oculta==palavra_secreta :
        print("Parabéns! Você acertou a palavra secreta.")
        break
else :
    print(f"Você perdeu! A palavra secreta era {(palavra_secreta).upper()}")