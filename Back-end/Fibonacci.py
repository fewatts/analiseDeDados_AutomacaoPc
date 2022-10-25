print('¬' * 11)
print(' Fibonacci ')
print('¬' * 11)
n1 = 0
n2 = 1
elements = 0
n = int(input('Digite quantos termos deseja ver: '))
print(f'{n1} ¬ {n2} ¬ ', end='')
elements = 2
while elements != n:
    n3 = n1 + n2
    print(f'{n3} ¬ ', end='')
    n1 = n2
    n2 = n3
    elements += 1
print('Fim', end='')
