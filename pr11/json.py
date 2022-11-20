from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import requests

DISPLAY_FONT = ("Arial", 30)
BUTTON_FONT = ("Arial", 25)

root=Tk()
root.title("Получение информации о репозитории")
root.geometry("600x430")
root.resizable(False,False)

def show_info():
    a = entry.get()
    url = f"https://api.github.com/users/{a}"
    r = requests.get(url).json()
    st = "company: "
    st+= str(r["company"])
    st+='\ncreated: '
    st+= str(r["created_at"])
    st+='\nemail: '
    st+= str(r["email"])
    st+='\nid: '
    st+=str(r["id"])
    st+='\nname: '
    st+=str(r["name"])
    st+='\nurl: '
    st+=str(r["url"])
    label["text"]=st
    with open("info.txt", "a+") as f:
        f.write(f"company: {r['company']}\n")
        f.write(f"created_at': {r['created_at']}\n")
        f.write(f"email: {r['email']}\n")
        f.write(f"id: {r['id']}\n")
        f.write(f"name: {r['name']}\n")
        f.write(f"url: {r['url']}\n")
        f.write("\n")

label_text=ttk.Label(text="Введите название репозитория")
label_text.pack()
entry = ttk.Entry()
entry.pack(anchor=NW, padx=150, pady=15,ipadx=90,ipady=10)
label = ttk.Label(text="")
label.pack(anchor=NW, padx=150, pady=15)
btn = ttk.Button(text="Запрос", command=show_info, width=50)
btn.pack(anchor=NW, padx=150, pady=15)


root.mainloop()

