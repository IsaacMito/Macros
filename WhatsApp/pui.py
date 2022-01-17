import threading
import time
from tkinter import *

def run():

    for i in range(0, 20000000000000000000000000000000000000000000000):

        listBox.insert(END, i)
        listBox.see("end")
        window.focus_set()

window = Tk()

window.title("WhatsApp")

lblTitle = Label(window, text="Console", font=("Courier", 14))

listBox = Listbox(window, height=10, width=52)
scrollbar = Scrollbar(window)

listBox.config(yscrollcommand=scrollbar.set)

threading.Thread(target=run).start()

lblTitle.pack()
scrollbar.pack(side=RIGHT, fill=BOTH)
listBox.pack()

window.mainloop()
