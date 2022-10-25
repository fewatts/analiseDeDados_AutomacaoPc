import pyautogui
import pyperclip
import pandas
from time import sleep
pyautogui.PAUSE = 3
#baixar a pasta de arquivos ok
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 't')
sleep(3)
pyperclip.copy('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
sleep(7)
pyautogui.click(x=474, y=455)
sleep(4)
pyautogui.click(x=719, y=936)
pyautogui.click(x=501, y=442)
pyautogui.click(x=1667, y=234)
pyautogui.click(x=1402, y=723)
sleep(10)
#calcular os indicadores
tabela = pandas.read_excel(r'C:\Users\Administrador\Downloads\Vendas - Dez.xlsx')
print(tabela)
quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()
#entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/?pli=1#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
sleep(10)
#mandar o email
pyautogui.click(x=66, y=255, clicks=2)
sleep(7)
pyperclip.copy('feralveswatts@gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
relatorio = (f'''Prezado/a segue o email do relatório de vendas:
Total de vendas: {quantidade:,.2f}
Faturamento total: {faturamento:,.2f}
Atts Python''')
pyperclip.copy(relatorio)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=1277, y=919, clicks=2)
#tudo OKKKKKKKKKKKKKKKKKKKKKK
