print('¬' * 18)
print(' CAIXA ELETRÔNICO ')
print('¬' * 18)
cinquenta = vinte = dez = um = 0
valor = int(input('Qual o valor a ser sacado? [temos notas de 50, 20, 10, 5 e 1] '))
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    elif valor == 0:
        break
print(f'''No total foram {cinquenta} cédula/s de 50
{vinte} cédula/s de 20
{dez} cédula/s de 10
e {um} cédula/s de 1''')
