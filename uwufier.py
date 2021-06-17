import re
import pyperclip
import tkinter as tk

#string = str(input("Pwease paste text hewe: "))
def uwu():
    string = pyperclip.paste()
    string = string.replace('r','w')
    string = string.replace("l","w")
    #string = string.replace("o","uwu")
    #string = re.sub("u\S","uwu",string)
    #string = re.sub("o\S","owo",string)
    pyperclip.copy(string)

root = tk.Tk()
b = tk.Button(root, text="Uwufy", command=uwu)
b.pack()

root.mainloop()

