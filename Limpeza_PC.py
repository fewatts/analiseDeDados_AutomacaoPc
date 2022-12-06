#para que o código funcione, deve ser executado em conta de administrador! (Se sua máquina tiver processador superior ao celeron, diminua o tempo de PAUSE e sleeps)
import pyautogui
import pyperclip
from time import sleep
pyautogui.PAUSE = 4
opção = 0
continuar = ''
aberto = ''

def memory():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('%temp%')
    pyautogui.hotkey('enter')
    sleep(4)
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
    sleep(130)
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


def logo():
    print("¬" * 40)
    print("         0TIMIZADOR DE SISTEMAS         ")
    print("¬" * 40)
    print("Para suporte entre em contato: feralveswatts@gmail.com")


def aguarde():
    print("  Processando dados... \n  Aguarde para continuar.")




#Programa_principal
logo()
while continuar in 'SN':
    while opção != 5:
        opção = int(input(''' 
    É indicado primeiro limpar a memória,
    fazer a checagem de sistema
    e por útimo, checagem de virus.
    Não mexa nas janelas enquanto processos
    estiverem sendo executados

    [1] Limpeza de memória (5-10 min)
    [2] Escaneamento do sistema (5-10 min)
    [3] Checagem de vírus (5-10 min)
    [4] Checagem completa do sistema (10-20 min)
    [5] Fechar sistema
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
            memoria()
            aguarde()
            sistem_scan()
            aguarde()
            virus_check()
            break
        elif opção == 5:
            break
        else:
            print(" Opção inválida, digite novamente!")
    continuar = str(input("Deseja continuar usando o programa? [S/N]  ")).strip().upper()[0]
    if continuar in 'N':
        break
logo()
print('Obrigado por usar meu programa! volte sempre!')
