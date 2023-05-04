import tkinter
from tkinter import *
from tkinter import ttk
import random as r
import json


root = Tk()
root.title("Job Info Helper")

# Variables
rowspace = 3
cbspacex = 3
Personal = {
    'fname' : tkinter.StringVar(),
    'lname' : tkinter.StringVar(),
    'addr' : tkinter.StringVar(),
    'city' : tkinter.StringVar(),
    'zip' : tkinter.StringVar(),
    'phone' : tkinter.StringVar(),
    'email' : tkinter.StringVar(),
    'uname' : tkinter.StringVar(root, "jun" + str(r.randint(99, 1000)) + "ny")
}


def submit():
    with open("job-assistant.txt", "w") as savefile:
        temp = str(({x: y.get() for (x, y) in Personal.items()})).replace("'",'"')
        savefile.write('%s\n' % temp)
        savefile.close()
    return


def loadInfo():
    with open("job-assistant.txt", "r") as loadfile:
        lines = loadfile.read().splitlines()

        for line in lines:
            if line.startswith('{"fname":'):
                loadDict(json.loads(line))

        loadfile.close()


def loadDict(tempDict):
    global Personal
    for key1 in Personal.keys():
        i = 0
        for key2 in tempDict.keys():
            i += 1
            if key1 == key2:
                a = tempDict[key1]
                Personal[key1].set(a)
                del tempDict[key1]
                print('Key loaded: %s %s %s' % (key1, key2, Personal[key1]))
                break
            print('Comparing: %s %s iteration %s' % (key1, key2, str(i)))


def copy(item):
    root.clipboard_clear()
    root.clipboard_append(item)
    root.update()


def unamegen():
    newuser = "jun" + str(r.randint(99, 1000)) + "ny"
    Personal["uname"].set(newuser)


frm = ttk.Frame(root, padding=15)
frm.grid()

# First Name
ttk.Label(frm, text="First Name").grid(column=0, row=0, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["fname"]).grid(column=1, row=0, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["fname"].get())).grid(column=2, row=0, pady=rowspace, padx=cbspacex)

# Last Name
ttk.Label(frm, text="Last Name").grid(column=0, row=1, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["lname"]).grid(column=1, row=1, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["lname"].get())).grid(column=2, row=1, pady=rowspace, padx=cbspacex)

# Address
ttk.Label(frm, text="Address").grid(column=0, row=2, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["addr"]).grid(column=1, row=2, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["addr"].get())).grid(column=2, row=2, pady=rowspace, padx=cbspacex)

# City
ttk.Label(frm, text="City").grid(column=0, row=3, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["city"]).grid(column=1, row=3, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["city"].get())).grid(column=2, row=3, pady=rowspace, padx=cbspacex)

# Zip Code
ttk.Label(frm, text="Zip Code").grid(column=0, row=4, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["zip"]).grid(column=1, row=4, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["zip"].get())).grid(column=2, row=4, pady=rowspace, padx=cbspacex)

# Phone Number
ttk.Label(frm, text="Phone Number").grid(column=0, row=5, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["phone"]).grid(column=1, row=5, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["phone"].get())).grid(column=2, row=5, pady=rowspace, padx=cbspacex)

# Email Address
ttk.Label(frm, text="Email Address").grid(column=0, row=6, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["email"]).grid(column=1, row=6, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["email"].get())).grid(column=2, row=6, pady=rowspace, padx=cbspacex)

# Username
ttk.Label(frm, text="Username").grid(column=0, row=7, pady=rowspace)
ttk.Entry(frm, textvariable=Personal["uname"], state=DISABLED).grid(column=1, row=7, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(Personal["uname"])).grid(column=2, row=7, padx=cbspacex)
ttk.Button(frm, text="Generate", command=unamegen).grid(column=2, row=8, padx=cbspacex)


# File save/load
ttk.Button(frm, text="Load", command=loadInfo).grid(column=0, row=9, pady=10)
ttk.Button(frm, text="Save", command=submit).grid(column=1, row=9, pady=10)




root.mainloop() #Puts everything above on display.