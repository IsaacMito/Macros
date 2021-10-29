import time

from selenium import webdriver
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

    def getContact(self, numero=""):

        if numero == "":
            self.navegador.get(f"https://web.whatsapp.com/")
        else:
            self.navegador.get(f"https://web.whatsapp.com/send?phone={numero}")

        while len(self.navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)

        time.sleep(2)

    def wasAnswered(self, texto, total_mensage_enviadas=1):
        try:
            div = self.navegador.find_element_by_class_name("y8WcF")
        except:
            return False

        while len(div.find_elements_by_css_selector(".message-out, .message-in")) < 1:
            time.sleep(1)

        for i in range(1, 3):
            div.send_keys(Keys.PAGE_UP)
            time.sleep(1)

        menssagens = div.find_elements_by_css_selector(".message-out, .message-in")

        texto_encontrado = bool()
        cont_msg_env = 1
        lista_msg_recebidas = list()

        for msg in menssagens:

            if "message-out" in msg.get_attribute("class"):

                if texto_encontrado:

                    if total_mensage_enviadas == cont_msg_env:

                        if len(lista_msg_recebidas) != 0:

                            return f"{lista_msg_recebidas[0]}  /  {lista_msg_recebidas[len(lista_msg_recebidas) - 1]}".replace(
                                "\n", " ")
                        else:
                            return False
                    else:
                        cont_msg_env += 1

                elif texto in msg.text:

                    texto_encontrado = True

            else:
                if texto_encontrado:
                    lista_msg_recebidas.append(msg.text)

        return False
