from random import randint
from time import sleep
print('¬¬¬¬¬¬¬¬¬¬¬¬ JO-KÊN-PO ¬¬¬¬¬¬¬¬¬¬¬¬')
jogador = int(input('''[0] PEDRA
[1] PAPEL
[2] TESOURA
>>>>>>>>>>>>>>Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!!!!!')
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}')
if computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
    print('JOGADOR vence!')
elif computador == jogador:
    print('EMPATE...')
else:
    print('COMPUTADOR vence!')
