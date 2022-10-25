from math import factorial
from time import sleep
print('¬' * 21)
print(' Cálculo de fatorial ')
print('¬' * 21)
while True: 
    num = int(input('Digite um número: [666 para parar] '))
    if num == 666:
        print('Encerrando...')
        sleep(4)
        break
    n = num
    print(f'O fatorial do número digitado é')
    print(f'{num}! = ', end='')
    for n in range(num, 0, -1):
        print(n, end='')
        print(' x ' if n > 1 else ' = ', end='')
    print(f'{factorial(num)}')
print('Obrigado por usar meu programa, volte sempre!')
