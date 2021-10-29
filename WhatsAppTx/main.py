from openpyxl import load_workbook

from WhatsAppTx import WhatsApp

path_exel = "C:\\Users\\DEV\\Desktop\\CalceContatos\\Controle\\DisparoClientesAsaSulControle-2021-09-08.xlsx"
arquivo_excel = load_workbook(path_exel)
plan = arquivo_excel.active
max_row = plan.max_row

TEXTO = "CALCE PERFEITO – CASH BACK"

ws = WhatsApp()
ws.getContact()

for r in range(1, max_row + 1):

    cell_num = plan.cell(column=1, row=r)
    cell_ok = plan.cell(column=2, row=r)
    cell_men = plan.cell(column=3, row=r)

    if cell_ok.value == "ok":

        if cell_men.value == None:

            numero = str(cell_num.value).replace("+55", "").replace(" ", "").replace("-", "")

            if len(numero) == 11:
                numero = numero[3:]

            elif len(numero) == 9:
                numero = numero[1:]

            if len(numero) != 12:
                numero = f"5561{numero}"
            print(f"{numero}", end=" ")

            ws.getContact(numero)
            cell_men.value = str(ws.wasAnswered(TEXTO))

            print(f": {cell_men.value}")

            arquivo_excel.save(path_exel)
