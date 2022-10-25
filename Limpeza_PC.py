#para que o código funcione, deve ser executado em conta de administrador! (Se sua máquina tiver processador superior ao celeron, diminua o tempo de PAUSE e sleeps)
import pyautogui
import pyperclip
from time import sleep
pyautogui.PAUSE = 6
#temp files
pyautogui.hotkey('win', 'r')
pyautogui.write('%temp%')
pyautogui.hotkey('enter')
sleep(4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
#disk cleanup
pyautogui.hotkey('win')
pyautogui.write('limpeza')
pyautogui.hotkey('enter')
sleep(130)
pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
sleep(130)
#Scannow 
pyautogui.hotkey('win')
pyautogui.write('cmd')
pyautogui.hotkey('enter')
sleep(3)
pyperclip.copy('SFC /SCANNOW')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
#check health
pyautogui.hotkey('win')
pyautogui.write('cmd')
pyautogui.hotkey('enter')
sleep(3)
pyperclip.copy('Dism /online /Cleanup-Image /CheckHealth')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
#MSoftware removal 
pyautogui.hotkey('win', 'r')
pyautogui.write('mrt')
pyautogui.hotkey('enter')
sleep(15)
pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
print('System check done, wait for processes to end')
