nome = str(input('digite o seu nome completo: ')).strip()
print('analisando o seu nome...')
print('o seu nome em maiúsculo é {}'.format(nome.upper()))
print('o seu nome em minúsculo é {}'.format(nome.lower()))
print('o seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('o seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0],(len(nome.split()[0]))))

#.format(nome.find(' ')) -> define quantas letras tem o primeiro nome, pois indica a posição do primeiro espaço (que separa o primeiro nome dos outros)