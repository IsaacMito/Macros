import time

import clipboard
import numpy
import numpy as np
import pyautogui
from cv2 import cv2

cd = "icons\\"

icSend = cd + "icon_send.png"
icAnex = cd + "icon_anex.png"
icPesq = cd + "icon_pesq.png"
icPesqBack = cd + "icon_pesq_back.png"

def pesquisar( str=""):
    #Procurando icon de pesquisa
    locale = pyautogui.locateOnScreen(icPesq, grayscale=True)

    if locale is None:
        locale = pyautogui.locateOnScreen(icPesqBack, grayscale=True)

    pyautogui.moveTo(locale)
    pyautogui.move(50, 0)
    click()

    #Selecionando e colando o nome
    pyautogui.hotkey("ctrl", "a")
    colar(str)
    time.sleep(0.5)

    #Entrando no contato
    pyautogui.press("enter")
    time.sleep(0.5)

    #Verivicando se o contato existe
    return isImgIgual()


def enviarARQ(pdr=""):
    click(icAnex)
    pyautogui.move(0, -50)
    click()
    time.sleep(0.26)
    colar(pdr)
    pyautogui.press("enter")
    click(icSend)


def enviarTX( str=""):
    colar(str)
    pyautogui.press("enter")


def click( icon=""):
    if icon == "":
        pyautogui.click()
    else:
        # Procurando Icon
        while True:
            try:
                pyautogui.click(icon)
                break
            except:
                pass


def colar(str=""):
    clipboard.copy(str)
    pyautogui.hotkey("ctrl", "v")


def isImgIgual():

    #Tira print da tela
    pyautogui.screenshot(region=[25,150,350,150]).save("img_com_pesq.png")
    time.sleep(0.1)

    img1 = cv2.imread("img_com_pesq.png", 0)
    img2 = cv2.imread("img_compare.png", 0)

    t = cv2.absdiff(img1, img2)
    res = t.astype(np.uint8)
    #Tirando percentual de difereça
    porcent = (numpy.count_nonzero(res) * 100) / res.size

    if porcent > 8:
        return True
    else:
        return False




