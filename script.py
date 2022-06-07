import pyautogui
import time
# codesnap 1559 184
print("Começando o programa...")
time.sleep(5)
nameFile = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

for i in range(15):
    pyautogui.hotkey('ctrl', 'a')
    # click no codesnap
    pyautogui.click(1559, 184)
    time.sleep(2)
    pyautogui.write(nameFile[i])
    pyautogui.press('del')
    pyautogui.press('enter')
    time.sleep(0.5)
    # click na tela para não fechar o codesnap
    pyautogui.click(721, 330)
    pyautogui.hotkey('ctrl', 'w')
