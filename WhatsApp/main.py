from time import sleep

from openpyxl import load_workbook

from Util import contain, InputKeys
import WhatsApp

texto = """*CALCE PERFEITO – COMPROU, ACHOU, GANHOU!*

É isso mesmo.
A nossa promoção
*Estoura Balão voltou!* 😍 🎉

*Você pode ganhar*
vale-presentes, 
kits de almofadas, 
necessaire, e muito mais!*

*Corra!* 
Essa promoção
é válida por tempo 
limitado! ⏳

*Para mais informações, é só nos chamar aqui no Whatsapp."""

xlsx_path = r"C:\Users\DEV\Desktop\CalceContatos\21-10-2021\ContatosAsaNorte.xlsx"
file_path = r"C:\Users\DEV\Desktop\CalceContatos\21-10-2021\WhatsApp Image 2021-10-20 at 13.48.45.jpeg"

xlsx = load_workbook(xlsx_path)
sheet = xlsx.active
max_row = sheet.max_row

input = InputKeys()

for r in range(1, max_row + 1):

    if input.executando:

        cell_num = sheet.cell(column=1, row=r)
        cell_ok = sheet.cell(column=2, row=r)

        print(f"{r} - {max_row}: {cell_num.value}", end=" ")
        if cell_ok.value is not None:
            print(f"{cell_ok.value}", end=" ")

        if cell_ok.value != "ok" and cell_ok.value != "!":

                #Retirando 619
                numero = str(cell_num.value)[3:]

                if not contain(numero):

                    if WhatsApp.pesquisar(numero):

                        sleep(0.2)
                        WhatsApp.colar(texto)
                        sleep(0.6)
                        WhatsApp.enviarARQ(file_path)
                        sleep(1.65)

                        cell_ok.value = "ok"
                        print("ok", end=" ")

                    else:

                        cell_ok.value = "!"
                        print("!", end=" ")
                else:

                    cell_ok.value = "ok"
                    print("ok", end=" ")

                xlsx.save(xlsx_path)

        print("")
    else:
        break

print("FIM")
