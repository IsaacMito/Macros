import sys
import threading
import keyboard

#xlsx_controle = load_workbook(
    #r"C:\Users\DEV\Desktop\CalceContatos\21-10-2021\ContatosControleAsaNorte.xlsx")
#sheet_controle = xlsx_controle.active
#max_row_controle = sheet_controle.max_row

#def contain(contato: str):

    #for r in range(1, max_row_controle + 1):

        #if contato in str(sheet_controle.cell(column=1, row=r).value):
            #return True

    #return False

class InputKeys():

    def __init__(self):
        self.executando = True
        threading.Thread(target=self.ouvidor).start()

    def ouvidor(self):
        while True:
            if keyboard.read_key() == "0":
                self.executando = False
                sys.exit(-1)