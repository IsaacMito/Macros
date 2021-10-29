from time import sleep

import clipboard
import pyautogui

src = r"C:\Users\DEV\Desktop\mp4"
cd = "\icons"
btn_explorar = cd + "explorar.PNG"
btn_play = cd + "play.PNG"
lb_titulo = cd + "titulo.PNG"

cont = 10
for i in range(1, 108):

    pyautogui.click(btn_explorar)
    sleep(0.1)
    clipboard.copy(fr"{src}\video{cont}.mp4")
    cont += 1
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sleep(0.1)
    pyautogui.click(btn_play)
    pyautogui.move(50, 50)

    while True:
        locale = pyautogui.locateOnScreen(btn_play, grayscale=True)
        if locale != None:
            break

    pyautogui.moveTo(lb_titulo)
    pyautogui.move(75, 0)
    pyautogui.click()
    sleep(0.2)
    pyautogui.move(0, 35)
    pyautogui.click()
