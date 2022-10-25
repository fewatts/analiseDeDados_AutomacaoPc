print('¬' * 20)
print(' LOJA SUPER BARATÃO ')
print('¬' * 20)
soma = count = mais_barato = 0
nome_mais_barato = ''
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preço = int(input('Qual o preço do produto? '))
    soma += preço
    if preço > 1000:
        count += 1
    if count == 1 or preço < mais_barato:
        mais_barato = preço
        nome_mais_barato = nome
    opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'''O total da compra foi de {soma:.2f} R$
Temos {count} produtos custando mais de mil reais
e o produto mais barato foi {nome_mais_barato} que custa {mais_barato}''')
