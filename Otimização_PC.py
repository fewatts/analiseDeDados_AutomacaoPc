#para que o código funcione, deve ser executado em conta de administrador! 
#(Se sua máquina tiver processador superior ao celeron, diminua o tempo de PAUSE e sleeps)
import pyautogui
import pyperclip
from time import sleep
pyautogui.PAUSE = 3
opção = 0
continuar = ''
aberto = ''


def memoria():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('%temp%')
    pyautogui.hotkey('enter')
    sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')
    pyautogui.hotkey('up')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('down')
    pyautogui.hotkey('right')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('win')
    pyautogui.write('limpeza')
    pyautogui.hotkey('enter')
    sleep(116)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')


def sistem_scan():
    pyautogui.hotkey('win')
    pyautogui.write('cmd')
    pyautogui.hotkey('enter')
    sleep(3)
    pyperclip.copy('SFC /SCANNOW')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('win')
    pyautogui.write('cmd')
    pyautogui.hotkey('enter')
    sleep(3)
    pyperclip.copy('Dism /online /Cleanup-Image /CheckHealth')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')


def virus_check():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('mrt')
    pyautogui.hotkey('enter')
    sleep(15)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')


def allvirus_check():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('mrt')
    pyautogui.hotkey('enter')
    sleep(15)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')


def logo():
    print("¬" * 50)
    print("              0TIMIZADOR DE SISTEMAS              ")
    print("¬" * 50)
    print("   Para suporte entre em contato: \n   feralveswatts@gmail.com")


def aguarde():
    print("   Processando dados... \n   Aguarde para continuar.")


#Programa_principal
logo()
print('''
    Para otimização total
    execute as opções na 
    seguinte ordem: 1; 2; 3 ou 4.
    Não mexa nas janelas
    enquanto processos estiverem 
    sendo executados.
    
    ATENÇÂO: 
    Antes de executar a limpeza de 
    memória, abra o app limpeza de disco
    e selecione as opções que deseja limpar,
    ao selecionar lixeira, fique
    atento a arquivos importantes contidos
    na mesma.''')
while continuar in 'SN':
    while opção != 6:
        opção = int(input(''' 
    [1] Limpeza de memória (5-8 min)
    [2] Escaneamento do sistema (10 min)
    [3] Checagem de vírus (10 min)
    [4] Checagem completa de vírus (pode levar horas)
    [5] Checagem completa do sistema (pode levar horas)
    [6] Fechar sistema
    Digite uma opção:   '''))
        if opção == 1:
            aguarde()
            memoria()
            break
        elif opção == 2:
            aguarde()
            sistem_scan()            
            break
        elif opção == 3:
            aguarde()
            virus_check()
            break
        elif opção == 4:
            aguarde()
            allvirus_check()
            break
        elif opção == 5:
            aguarde()
            memoria()
            sleep(15)
            aguarde()
            sistem_scan()
            sleep(15)
            aguarde()
            allvirus_check()
            break
        elif opção == 6:
            break
        else:
            print("  Opção inválida, digite novamente!")
    continuar = str(input("   Deseja continuar usando o programa? [S/N]  ")).strip().upper()[0]
    if continuar in 'N':
        break
logo()
print('Obrigado por usar meu programa! volte sempre!')
