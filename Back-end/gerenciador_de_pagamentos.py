print('¬¬¬¬¬¬¬¬¬¬ Loja watts ¬¬¬¬¬¬¬¬¬¬')
compras = float(input('Qual o valor das compras? R$'))
opção = int(input('''[1] À vista no dinheiro (10% de desconto)
[2] À vista no cartão débito (5% de desconto)
[3] Em até 2x no cartão de crédito (sem desconto)
[4] Em 3x ou mais no cartão de crédito (20% de juros)
Sua opção: '''))
if opção == 1:
    print(f'O valor a ser pago com o desconto é de {compras - (compras * 0.1):.2f} R$')
elif opção == 2:
    print(f'O valor a ser pago é de {compras - (compras * 0.05):.2f} R$')
elif opção == 3:
    print(f'Serão no total, duas parcelas mensais de {compras / 2:.2f} R$\nSendo no total {compras} R$')
elif opção == 4:
    vezes = int(input('Serão quantas parcelas? '))
    print(f'Serão no total {vezes} parcelas no valor de {(compras + (compras * 0.2)) / vezes} R$\nO total será de {(compras + (compras * 0.2))}')
else:
    print('Opção inválida!')
