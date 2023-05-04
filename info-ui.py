import tkinter
import random as r
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Job Info Helper")

# Variables
rowspace = 3
cbspacex = 3
fname = tkinter.StringVar()
lname = tkinter.StringVar()
addr = tkinter.StringVar()
city = tkinter.StringVar()
zip = tkinter.StringVar()
phone = tkinter.StringVar()
email = tkinter.StringVar()
uname = tkinter.StringVar(root, "jun" + str(r.randint(99, 1000)) + "ny")

def submit():
    print("First Name: " + fname.get())
    print("Last Name: " + lname.get())
    print("Address: " + addr.get())
    print("Zip Code: " + zip.get())
    print("Phone #: " + phone.get())
    print("Email: " + email.get())
    print("Username: " + uname.get())


def copy(item):
    root.clipboard_clear()
    root.clipboard_append(item)
    root.update()

def unamegen():
    newuser = "jun" + str(r.randint(99, 1000)) + "ny"
    uname.set(newuser)


frm = ttk.Frame(root, padding=15)
frm.grid()

# First Name
ttk.Label(frm, text="First Name").grid(column=0, row=0, pady=rowspace)
ttk.Entry(frm, textvariable=fname).grid(column=1, row=0, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(fname.get())).grid(column=2, row=0, pady=rowspace, padx=cbspacex)

# Last Name
ttk.Label(frm, text="Last Name").grid(column=0, row=1, pady=rowspace)
ttk.Entry(frm, textvariable=lname).grid(column=1, row=1, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(lname.get())).grid(column=2, row=1, pady=rowspace, padx=cbspacex)

# Address
ttk.Label(frm, text="Address").grid(column=0, row=2, pady=rowspace)
ttk.Entry(frm, textvariable=addr).grid(column=1, row=2, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(addr.get())).grid(column=2, row=2, pady=rowspace, padx=cbspacex)

# City
ttk.Label(frm, text="City").grid(column=0, row=3, pady=rowspace)
ttk.Entry(frm, textvariable=city).grid(column=1, row=3, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(city.get())).grid(column=2, row=3, pady=rowspace, padx=cbspacex)

# Zip Code
ttk.Label(frm, text="Zip Code").grid(column=0, row=4, pady=rowspace)
ttk.Entry(frm, textvariable=zip).grid(column=1, row=4, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(zip.get())).grid(column=2, row=4, pady=rowspace, padx=cbspacex)

# Phone Number
ttk.Label(frm, text="Phone Number").grid(column=0, row=5, pady=rowspace)
ttk.Entry(frm, textvariable=phone).grid(column=1, row=5, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(phone.get())).grid(column=2, row=5, pady=rowspace, padx=cbspacex)

# Email Address
ttk.Label(frm, text="Email Address").grid(column=0, row=6, pady=rowspace)
ttk.Entry(frm, textvariable=email).grid(column=1, row=6, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(email.get())).grid(column=2, row=6, pady=rowspace, padx=cbspacex)

# Username
ttk.Label(frm, text="Username").grid(column=0, row=7, pady=rowspace)
ttk.Entry(frm, textvariable=uname, state=DISABLED).grid(column=1, row=7, pady=rowspace)
ttk.Button(frm, text="Copy", command=lambda: copy(uname)).grid(column=2, row=7, padx=cbspacex)
ttk.Button(frm, text="Generate", command=unamegen).grid(column=2, row=8, padx=cbspacex)


# Update Values
ttk.Button(frm, text="Update", command=submit).grid(column=1, row=9, pady=10)




root.mainloop() #Puts everything above on display.