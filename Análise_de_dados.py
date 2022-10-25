maiores_dezoito = homens = mulheres_maiores = 0
while True:
    print('¬' * 21)
    print(' CADASTRE UMA PESSOA ')
    print('¬' * 21)
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo?[M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo?[M/F] ')).strip().upper()[0]
    if idade >= 18:
        maiores_dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >= 20:
        mulheres_maiores += 1
    opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'''No total foram {maiores_dezoito} pessoas com 18 anos ou mais,
{homens} Pessoas do sexo masculino
e {mulheres_maiores} mulheres com 20 anos ou mais.''')
