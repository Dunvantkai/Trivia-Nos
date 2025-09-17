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
        servers = []
    try:
        with open("serverlist.json", "w") as f:
            json.dump(servers, f, indent=4)
    except PermissionError:
        print("Issue creating serverlist.json")

def jointab():
    join_bg_photo = Image.open("Backgrounds/Lobby.png")
    join_bg_photo = join_bg_photo.resize((1600, 800), Image.Resampling.LANCZOS)
    join_bg = ImageTk.PhotoImage(join_bg_photo)
    bg_label = tk.Label(joinTab, image=join_bg)
    bg_label.image = join_bg  # Keep a reference!
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    titleArm1 = tk.Frame(joinTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm1.place(relx=0.42, rely=0.00, anchor="n")
    titleArm2 = tk.Frame(joinTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm2.place(relx=0.54, rely=0.00, anchor="n")
    title = Label(joinTab, text="Trivia-Nos", font=("Algerian", 40), padx=10, pady=10, bd=5, relief="solid", bg="lightgray")
    title.place(relx=0.48, rely=0.03, anchor="n")
    notebook.select(joinTab)
    print("Join Tab Selected")

def splashtab():
    splash_bg_photo = Image.open("Backgrounds/Lobby.png")
    splash_bg_photo = splash_bg_photo.resize((1600, 800), Image.Resampling.LANCZOS)
    splash_bg = ImageTk.PhotoImage(splash_bg_photo)
    bg_label = tk.Label(splashTab, image=splash_bg)
    bg_label.image = splash_bg  # Keep a reference!
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    titleArm1 = tk.Frame(splashTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
    titleArm1.place(relx=0.42, rely=0.00, anchor="n")
    titleArm2 = tk.Frame(splashTab, height=25, width=10.5, bd=2, relief="solid", bg="lightgray")
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