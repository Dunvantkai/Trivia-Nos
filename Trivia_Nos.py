from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import os
from PIL import Image, ImageTk
#  -- Builds Window
root = tk.Tk()
root.title("Trivia Nos")
root.geometry("1600x800")
root.resizable(width=False, height=False)
# -- hide tabs
style = ttk.Style()
style.layout("TNotebook", [])
style.layout("TNotebook.Tab", [])
# -- builds tabs
notebook = ttk.Notebook(root)
joinTab = Frame(notebook)
notebook.add(joinTab, text="Join")
lobbyTab = Frame(notebook)
notebook.add(lobbyTab, text="Lobby")
addServerTab = Frame(notebook)
notebook.add(addServerTab, text="Add_Server")
splashTab = Frame(notebook)
notebook.add(splashTab, text="Splash")
notebook.pack(expand=1, fill="both")
# -- server
servers = []

def serverlist():
    global servers
    try:
        with open("serverlist.json", "r") as f:
            servers = json.load(f)
    except FileNotFoundError:
        servers = [ {"name": "Local Host", "ip": "127.0.0.1", "port": 25565} ]
    try:
        with open("serverlist.json", "w") as f:
            json.dump(servers, f, indent=4)
    except PermissionError:
        print("Issue creating serverlist.json")

def serveraddtab():
    join_bg_photo = Image.open("Backgrounds/Lobby.png")
    join_bg_photo = join_bg_photo.resize((1600, 800), Image.Resampling.LANCZOS)
    join_bg = ImageTk.PhotoImage(join_bg_photo)
    bg_label = Label(addServerTab, image=join_bg)
    bg_label.image = join_bg  # Keep a reference!
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    titleArm1 = Frame(addServerTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm1.place(relx=0.42, rely=0.00, anchor="n")
    titleArm2 = Frame(addServerTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm2.place(relx=0.54, rely=0.00, anchor="n")
    title = Label(addServerTab, text="Trivia-Nos", font=("Algerian", 40), padx=10, pady=10, bd=5, relief="solid", bg="lightgray")
    title.place(relx=0.48, rely=0.03, anchor="n")
    # -- tab name
    tabArm1 = Frame(addServerTab, height=22, width=10, bd=2, relief="solid", bg="lightgray")
    tabArm1.place(relx=0.44, rely=0.14, anchor="n")
    tabArm2 = Frame(addServerTab, height=22, width=10, bd=2, relief="solid", bg="lightgray")
    tabArm2.place(relx=0.52, rely=0.14, anchor="n")
    tabname = Label(addServerTab, text="Servers", font=("Algerian", 30), padx=10, pady=2, bd=5, relief="solid", bg="lightgray")
    tabname.place(relx=0.48, rely=0.1682, anchor="n")

    awindow = Frame(addServerTab, bg="#0d3b63", height=420, width=311, bd=3, relief="solid")
    awindow.place(relx=0.48, rely=0.55, anchor="center")
    nameTextBox = Entry(awindow, width=25)  
    nameTextBox.place(relx=0.5, rely=0.2, anchor="center")
    ipTextBox = Entry(awindow, width=25)
    ipTextBox.place(relx=0.5, rely=0.4, anchor="center")
    portTextBox = Entry(awindow, width=25)
    portTextBox.place(relx=0.5, rely=0.6, anchor="center")

    save = Button(awindow, text="Save", command=lambda: save_server(nameTextBox.get(), ipTextBox.get(), portTextBox.get()), font=("Arial", 20,), bd=3, relief="solid", bg="lightgray")
    save.place(relx=0.7, rely=0.9, anchor="center")
    back = Button(awindow, text="Back", command=jointab, font=("Arial", 20,), bd=3, relief="solid", bg="lightgray")
    back.place(relx=0.3, rely=0.9, anchor="center")

    notebook.select(addServerTab)
    print("Add Server Tab Selected")

def save_server(name, ip, port):
    print(name, ip, port)
    newServer = {f"name": {name}, "ip": {ip}, "port": {port}}
    servers.append(newServer)
    
def jointab():
    join_bg_photo = Image.open("Backgrounds/Lobby.png")
    join_bg_photo = join_bg_photo.resize((1600, 800), Image.Resampling.LANCZOS)
    join_bg = ImageTk.PhotoImage(join_bg_photo)
    bg_label = Label(joinTab, image=join_bg)
    bg_label.image = join_bg  # Keep a refrance!
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    titleArm1 = Frame(joinTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm1.place(relx=0.42, rely=0.00, anchor="n")
    titleArm2 = Frame(joinTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm2.place(relx=0.54, rely=0.00, anchor="n")
    title = Label(joinTab, text="Trivia-Nos", font=("Algerian", 40), padx=10, pady=10, bd=5, relief="solid", bg="lightgray")
    title.place(relx=0.48, rely=0.03, anchor="n")
    # -- tab name
    tabArm1 = Frame(joinTab, height=22, width=10, bd=2, relief="solid", bg="lightgray")
    tabArm1.place(relx=0.44, rely=0.14, anchor="n")
    tabArm2 = Frame(joinTab, height=22, width=10, bd=2, relief="solid", bg="lightgray")
    tabArm2.place(relx=0.52, rely=0.14, anchor="n")
    tabname = Label(joinTab, text="Servers", font=("Algerian", 30), padx=10, pady=2, bd=5, relief="solid", bg="lightgray")
    tabname.place(relx=0.48, rely=0.1682, anchor="n")
    # -- box
    jwindow = Frame(joinTab, bg="#0d3b63", height=420, width=311, bd=3, relief="solid") # width 311 #7b3e18
    jwindow.place(relx=0.48, rely=0.55, anchor="center")
    listbox = Listbox(jwindow, bg="lightgray", bd=3, relief="solid", highlightthickness=0)
    listbox.place(relx=0.5, rely=0.44, relwidth=0.9, relheight=0.8, anchor="center")
    buttonbox = Frame(jwindow, bg="#0d3b63", height=60, width=290)
    buttonbox.place(relx=0.5, rely=0.92, anchor="center")
    addbutton = Button(buttonbox, text="Add", command=serveraddtab, font=("Arial", 20,), bd=3, relief="solid", bg="lightgray")
    addbutton.place(relx=0.155, rely=0.5, anchor="center")
    joinbutton = Button(buttonbox, text="Join", command=serveraddtab, font=("Arial", 20), bd=3, relief="solid", bg="grey")
    joinbutton.place(relx=0.47, rely=0.5, anchor="center")
    rendbutton = Button(buttonbox, text="Rend", command=serveraddtab, font=("Arial", 20,), bd=3, relief="solid", bg="lightgray")
    rendbutton.place(relx=0.815, rely=0.5, anchor="center")

    for index, server in enumerate(servers):
        display_text = f" {index} {server['name']} IP: {server['ip']}"
        listbox.insert(tk.END, display_text)

    notebook.select(joinTab)
    print("Join Tab Selected")

def splashtab():
    splash_bg_photo = Image.open("Backgrounds/Lobby.png")
    splash_bg_photo = splash_bg_photo.resize((1600, 800), Image.Resampling.LANCZOS)
    splash_bg = ImageTk.PhotoImage(splash_bg_photo)
    bg_label = Label(splashTab, image=splash_bg)
    bg_label.image = splash_bg  # Keep a reference!
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    titleArm1 = Frame(splashTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm1.place(relx=0.42, rely=0.00, anchor="n")
    titleArm2 = Frame(splashTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm2.place(relx=0.54, rely=0.00, anchor="n")
    title = Label(splashTab, text="Trivia-Nos", font=("Algerian", 40), padx=10, pady=10, bd=5, relief="solid", bg="lightgray")
    title.place(relx=0.48, rely=0.03, anchor="n")
    Button(splashTab, text="▶", command=jointab, font=("bold", 40), padx=60, pady=2, bd=5, relief="solid", bg="lightgray").place(relx=0.48, rely=0.5, anchor="center")
    notebook.select(splashTab)
    print("Splash Tab Selected")


def main():
    serverlist()
    splashtab()

main()
root.mainloop()