import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WhatsApp:

    def __init__(self):

        file = open("session.txt")
        session_id = file.readline()

        if len(session_id) == 0:

            self.navegador = webdriver.Chrome(port=9515)

            file = open('session.txt', 'w')
            file.write(self.navegador.session_id)
            print(self.navegador.command_executor._url)

        else:

            self.navegador = webdriver.Remote(command_executor="http://127.0.0.1:9515")
            self.navegador.close()
            self.navegador.session_id = session_id

        self.navegador.get(f"https://web.whatsapp.com/")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)

    def getContact(self, numero=""):

        self.navegador.get(f"https://web.whatsapp.com/send?phone={numero}")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)

        time.sleep(4)

        if len(self.navegador.find_elements(by=By.CLASS_NAME, value="_3J6wB")) == 0:
            return True

        return False

    def wasAnswered(self, texto, total_mensage_enviadas=1):

        div = self.navegador.find_element(by=By.CLASS_NAME, value="y8WcF")

        while len(div.find_elements(by=By.CSS_SELECTOR, value=".message-out, .message-in")) < 1:
            time.sleep(1)

        for i in range(1, 3):
            div.send_keys(Keys.PAGE_UP)
            time.sleep(1)

        menssagens = div.find_elements(by=By.CSS_SELECTOR, value=".message-out, .message-in")

        texto_encontrado = bool()
        cont_msg_env:int = 1
        lista_msg_recebidas = list()

        for msg in menssagens:

            if "message-out" in msg.get_attribute("class"):

                if texto in msg.text:

                    texto_encontrado = True

                    if total_mensage_enviadas == cont_msg_env:

                        check = msg.find_elements(by=By.CLASS_NAME, value="do8e0lj9")[0]
                        check = check.find_elements(by=By.TAG_NAME, value="span")[0]

                        if "Enviada" in check.get_attribute("aria-label"):
                            return ("Nao", "")

                    else:
                        cont_msg_env += 1
            else:
                if texto_encontrado:
                    lista_msg_recebidas.append(msg.text)

        if len(lista_msg_recebidas) > 0:

            if len(lista_msg_recebidas) == 1:
                print()

                return ("Sim", lista_msg_recebidas[0][:len(lista_msg_recebidas[0]) - 5].replace("\n", " "))
            else:
                return ("Sim",
                        f"{lista_msg_recebidas[0][:len(lista_msg_recebidas[0]) - 5]}  |  {lista_msg_recebidas[len(lista_msg_recebidas) - 1][:len(lista_msg_recebidas[0]) - 5]}".replace(
                            "\n", " "))
        else:
            return ("Sim", "")
