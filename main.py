#!/usr/bin/python
from tkinter import *
from hasher.myhash import hashify
import tkinter as tk
import tkinter.scrolledtext as st
import pyperclip

state, counter, csize = 0, 0, 0
globalFont = ('Helvetica', 15, 'bold')
seedState = False
text_to_copy = None


def customHasher(event=None):
    global state
    password = onEnter2.get()
    printSeedHash(array=hashify(password=password))


def setSize(event=None):
    global counter, state, csize, seedState
    tempsize = csize
    size.set(onEnter.get())

    try:
        csize = size.get()
    except Exception:
        csize = 10

    if counter == 0:
        state = hashify(size=csize)
        counter += 1
    elif tempsize != csize:
        counter = 0
        state = hashify(size=csize)
        counter += 1

    printSeedHash(array=state)


def _algorithm():
    return algorithm.get()


def printSeedHash(array):
    global state
    global text_to_copy
    total = ["blake2b", "blake2s", "md5", "sha1", "sha224", "sha256",
             "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512"]

    globalSeedMessage = "Seed: "
    hashMessage = "Hash"

    def globalHashMessage(n):
        global text_to_copy
        return f"{hashMessage}({total[n]})   {array[1][total[n]]}"

    print(globalHashMessage(n=algorithm.get()))

    # blake2b
    if algorithm.get() == 0:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(0)}""")
        text_to_copy = globalHashMessage(0)
    # blake2s
    elif algorithm.get() == 1:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(1)}""")
        text_to_copy = globalHashMessage(1)
    # md5
    elif algorithm.get() == 2:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(2)}""")
        text_to_copy = globalHashMessage(2)
    # sha1
    elif algorithm.get() == 3:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(3)}""")
        text_to_copy = globalHashMessage(3)
    # sha224
    elif algorithm.get() == 4:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(4)}""")
        text_to_copy = globalHashMessage(4)
    # sha256
    elif algorithm.get() == 5:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(5)}""")
        text_to_copy = globalHashMessage(5)
    # sha384
    elif algorithm.get() == 6:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(6)}""")
        text_to_copy = globalHashMessage(6)
    # sha3_224
    elif algorithm.get() == 7:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(7)}""")
        text_to_copy = globalHashMessage(7)
    # sha3_256
    elif algorithm.get() == 8:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"{globalHashMessage(8)}")
        text_to_copy = globalHashMessage(8)
    # sha3_384
    elif algorithm.get() == 9:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"{globalHashMessage(9)}")
        text_to_copy = globalHashMessage(9)
    # sha3_512
    elif algorithm.get() == 10:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"{globalHashMessage(10)}")
        text_to_copy = globalHashMessage(10)
    # sha512
    elif algorithm.get() == 11:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"{globalHashMessage(11)}")
        text_to_copy = globalHashMessage(11)
    else:
        seed.configure(text=f"{globalSeedMessage}{array[0]}", font=globalFont)
        _hash.delete('1.0', END)
        _hash.insert(INSERT, f"""{globalHashMessage(5)}""")
        text_to_copy = globalHashMessage(5)


def textCopy():
    global text_to_copy
    if text_to_copy is not None and isinstance(text_to_copy, str):
        pyperclip.copy(text_to_copy.split(' ')[-1])
        pyperclip.paste()


root = Tk()
root.geometry("600x500")
root.title("Hash it")
root['bg'] = '#0A0A0A'

algorithm = IntVar()
hash = StringVar()
key = StringVar()
size = IntVar()
customPass = StringVar()


tk.Label(root, text="Enter Password", font=('calibre', 15, 'bold'), bg='#0A0A0A', fg='#FFFFFF').place(x=80, y=20)
onEnter2 = Entry(root, font=('calibre', 15, 'bold'), bg='#212121', fg='red')
onEnter2.bind("<Return>", customHasher)
onEnter2.place(x=250, y=20)


tk.Label(root, text="OR", font=('calibre', 10, 'bold'), bg='#0A0A0A', fg='#FFFFFF').place(x=350, y=50)

tk.Label(root, text="Password Length ", font=('calibre', 15, 'bold'), bg='#0A0A0A', fg='#FFFFFF').place(x=70, y=70)
onEnter = Entry(root, font=('calibre', 15, 'bold'), bg='#212121', fg='red')
onEnter.bind("<Return>", setSize)
onEnter.place(x=250, y=70)


# row 1
R0 = Radiobutton(root, text="BLAKE2B", variable=algorithm, value=0, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R0.place(x=100, y=110)
R1 = Radiobutton(root, text="BLAKE2S", variable=algorithm, value=1, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R1.place(x=200, y=110)
R2 = Radiobutton(root, text="MD5", variable=algorithm, value=2, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R2.place(x=300, y=110)
R3 = Radiobutton(root, text="SHA1", variable=algorithm, value=3, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R3.place(x=400, y=110)

# row 2
R4 = Radiobutton(root, text="SHA224", variable=algorithm, value=4, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R4.place(x=100, y=130)
R5 = Radiobutton(root, text="SHA256", variable=algorithm, value=5, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R5.place(x=200, y=130)
R6 = Radiobutton(root, text="SHA384", variable=algorithm, value=6, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R6.place(x=300, y=130)
R7 = Radiobutton(root, text="SHA3_224", variable=algorithm, value=7, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R7.place(x=400, y=130)

# row 3
R8 = Radiobutton(root, text="SHA3_256", variable=algorithm, value=8, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R8.place(x=100, y=150)
R9 = Radiobutton(root, text="SHA3_384", variable=algorithm, value=9, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R9.place(x=200, y=150)
R10 = Radiobutton(root, text="SHA3_512", variable=algorithm, value=10, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R10.place(x=300, y=150)
R11 = Radiobutton(root, text="SHA512", variable=algorithm, value=11, command=_algorithm, bg='#0A0A0A', fg='#FFFFFF', selectcolor='red')
R11.place(x=400, y=150)

seed = Label(root, bg='#0A0A0A', fg='red')
seed.place(x=100, y=180)

_hash = st.ScrolledText(root, width=50, height=8, font=("Times New Roman", 15), bg='#212121', foreground='red')
_hash.place(x=30, y=220)


def seedChange():
    global csize, state
    if csize <= 0:
        csize = 10
    try:
        newState = hashify(size=csize)
        state = newState
        return printSeedHash(array=newState)
    except Exception:
        return printSeedHash(array=hashify(size=10))


seedChangeButton = Button(text="ChangeSeed", command=seedChange, font=('calibre', 12, 'bold'), bg='#0A0A0A', fg='#FFFFFF')
seedChangeButton.place(x=150, y=410)

textCopyButton = Button(text="Copy to Clipboard", command=textCopy, font=('calibre', 12, 'bold'), bg='#0A0A0A', fg='#FFFFFF')
textCopyButton.place(x=300, y=410)

root.mainloop()
