import os
import threading
from random import randint
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def run_cracker():
    pas = password_entry.get()

    keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S  ", "T", "U", "V", "W", "X", "Y", "Z", "~", "`", "!", "@", "#",
           "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|",
           ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]

    psd = ""
    output_box.insert(tk.END, "\t\tAttacking...\n")
    output_box.insert(tk.END, "\t\tPlease wait...\n")

    while psd != pas:
        psd = ""
        for i in range(len(pas)):
            guessspass = keys[randint(0, 4)]
            psd = str(guessspass) + str(psd)

        output_box.insert(tk.END, psd + "\n")
        output_box.see(tk.END)

    output_box.insert(tk.END, "Password Cracked: " + psd + "\n")
    output_box.insert(tk.END, "\tPassword Cracked Successfully.\n")

def start_thread():
    threading.Thread(target=run_cracker, daemon=True).start()


OFF_BLACK = "#0b0f14"
PANEL_BLACK = "#0d1117"
GREEN = "#22c55e"
TEXT = "#e5e7eb"

root = tk.Tk()
root.title("Password Cracker")
root.geometry("400x300")
root.configure(bg=OFF_BLACK)

root.attributes("-alpha", 0.94)

tk.Label(
    root,
    text="Enter Password to Crack",
    fg=TEXT,
    bg=OFF_BLACK,
    font=("Segoe UI", 12)
).pack(pady=10)

password_entry = tk.Entry(
    root,
    width=25,
    show="*",
    font=("Segoe UI", 11),
    bg="#000000",
    fg=GREEN,
    insertbackground=GREEN,
    relief="flat"
)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Start Attack",
    command=start_thread,
    bg="#022c22",
    fg=GREEN,
    font=("Segoe UI", 11),
    relief="flat",
    padx=14
).pack(pady=10)

output_box = ScrolledText(
    root,
    height=12,
    bg=PANEL_BLACK,
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas", 10),
    relief="flat"
)
output_box.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
