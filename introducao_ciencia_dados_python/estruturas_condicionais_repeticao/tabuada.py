number = float(input('digite um número: '))
cont = 0
print('====== tabuada do {} ======'.format(int(number)))
while cont<=10 :
    result = number*cont
    print ('{} x {} = {}'.format(number, cont, result))
    cont = cont + 1