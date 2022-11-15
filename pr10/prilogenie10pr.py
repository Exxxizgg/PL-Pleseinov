from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

DISPLAY_FONT = ("Arial", 30)
BUTTON_FONT = ("Arial", 25)

root=Tk()
root.title("Плесеинов Максим Михайлович")
root.geometry("600x430")
root.resizable(False,False)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1,text="Калькулятор")
tab_control.add(tab2,text="Чекбоксы")
tab_control.add(tab3,text="Работа с текстом")

lb1=ttk.Label(tab1)
tab_control.pack(expand=1,fill="both")
lb2=ttk.Label(tab2)
tab_control.pack(expand=1,fill="both")
lb3=ttk.Label(tab3)
tab_control.pack(expand=1,fill="both")

# калькулятор

# Логика калькулятора
def calculate():
    try:
        result = eval(display.get())
        input_text.set(result)
    except:
        input_text.set("Ошибка!")

# дисплей
input_text = tk.StringVar()
display = tk.Entry(tab1, font=DISPLAY_FONT, textvariable=input_text, bg="azure", fg="black", width=28)
display.grid(row=0, columnspan=4, ipady=10)

# Кнопки
# кнопки1
tk.Button(tab1, text="(", font=BUTTON_FONT, fg="black", bg="medium aquamarine", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("("))).grid(row=1, column=0)
tk.Button(tab1, text=")", font=BUTTON_FONT, fg="black", bg="medium aquamarine", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(")"))).grid(row=1, column=1)
tk.Button(tab1, text="С", font=BUTTON_FONT, fg="black", bg="medium aquamarine", width=5, height=1, command=lambda: display.delete(len(display.get())-1)).grid(row=1, column=2)
tk.Button(tab1, text="=", font=BUTTON_FONT, fg="black", bg="light blue", width=5, height=1, command=calculate).grid(row=1, column=3)

# кнопки2
tk.Button(tab1, text="1", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(1))).grid(row=2, column=0)
tk.Button(tab1, text="2", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(2))).grid(row=2, column=1)
tk.Button(tab1, text="3", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(3))).grid(row=2, column=2)
tk.Button(tab1, text="+", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("+"))).grid(row=2, column=3)

# кнопки3
tk.Button(tab1, text="4", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(4))).grid(row=3, column=0)
tk.Button(tab1, text="5", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(5))).grid(row=3, column=1)
tk.Button(tab1, text="6", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(6))).grid(row=3, column=2)
tk.Button(tab1, text="-", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("-"))).grid(row=3, column=3)

# кнопки4
tk.Button(tab1, text="7", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(7))).grid(row=4, column=0)
tk.Button(tab1, text="8", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(8))).grid(row=4, column=1)
tk.Button(tab1, text="9", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(9))).grid(row=4, column=2)
tk.Button(tab1, text="x", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("*"))).grid(row=4, column=3)

# кнопки5
tk.Button(tab1, text="C", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: input_text.set("")).grid(row=5, column=0)
tk.Button(tab1, text="0", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(0))).grid(row=5, column=1)
tk.Button(tab1, text=".", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("."))).grid(row=5, column=2)
tk.Button(tab1, text="/", font=BUTTON_FONT, fg="black", bg="plum1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("/"))).grid(row=5, column=3)

services = []

def showInfo():
    for i in range(len(services)):
        selected = ""
        if services[i].get()>=1:
            selected+= str(i)
            messagebox.showinfo(message="Вы выбрали чекбокс " + selected)

for i in range(1,5):
    option = IntVar()
    option.set(0)
    services.append(option)

Checkbutton(tab2, text="Чекбокс 1",
variable = services[1]).pack()
Checkbutton(tab2, text="Чекбокс 2",
variable = services[2]).pack()
Checkbutton(tab2, text="Чекбокс 3",
variable = services[3]).pack()

Button(tab2,text="Проверить выбор",
command=showInfo).pack()


my_text = Text(tab3, width=60, height=20)
my_text.pack(pady=20)

def clear():
    my_text.delete(1.0, END)

button_frame = Frame(tab3)
button_frame.pack()



def open_file():
    file = fd.askopenfilename()
    with open(file, "r+", encoding="utf-8-sig") as f:
        line = f.read()
        my_text.insert("1.0", line)
        my_text.place(x=0,y=0)


menu = Menu(tab3)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="Открыть",command=open_file)
new_item.add_separator()
menu.add_cascade(label="Файл",menu=new_item)
root.config(menu=menu)


root.mainloop()

