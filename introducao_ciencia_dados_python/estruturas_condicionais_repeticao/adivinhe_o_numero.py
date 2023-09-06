from random import randint
num = randint(1,100)
chute = int(input('Adivinhe o número secreto entre 0 e 100: '))

while chute != num :
    if chute>num :
        print('O número secreto é menor que {}. Tente novamente!'.format(chute))
        chute = int(input('Adivinhe o número: '))
    else :
        if chute<num :
            print('O número secreto é maior que {}. Tente novamente!'.format(chute))
            chute = int(input('Adivinhe o número: '))        
else :
    print('Acertou!')