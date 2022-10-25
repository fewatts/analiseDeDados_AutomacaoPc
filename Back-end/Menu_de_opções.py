from time import sleep
n1 = int(input('Digite o 1ª número: '))
n2 = int(input('Digite o 2ª número: '))
while True:
    option = int(input('''>>>>Qual a sua opção?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
>>>>:  '''))
    if option == 1:
        print(f'A soma dos valores {n1} e {n2} é {n1 + n2}')
    elif option == 2:
        print(f'A multiplicação dos valores {n1} e {n2} é {n1 * n2}')
    elif option == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n1 == n2:
            print(f'Os números {n1} e {n2} são iguais')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
    elif option == 4:
        n1 = int(input('Digite o 1ª número: '))
        n2 = int(input('Digite o 2ª número: '))
    elif option == 5:
        print('ENCERRANDO...')
        sleep(4)
        break
    else:
        print('Opção inválida, tente novamente!')
print('Obrigado por usar meu programa! volte sempre!')
