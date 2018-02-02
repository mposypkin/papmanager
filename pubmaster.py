from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import bibtags

root = Tk()

#pubnames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada',
#'China', 'Denmark', 'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico',
#'Netherlands', 'Norway', 'Spain', 'Sweden', 'Switzerland')
pubnames = ()


def loadPubs():
    name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(("json files", "*.json"), ("all files", "*.*")))
    with open(name) as f:
        s = f.read();
    lbox.delete(0, END)
    parsed = json.loads(s)
    contrs = parsed['contributions']
    i = 0
    for contr in contrs:
        lbox.insert(i, str(i + 1) + ". " + contr[bibtags.title])
        if i % 2 :
            lbox.itemconfigure(i, background='#f0f0ff')
        i = i + 1

def savePubs():
    print("Hello");

pbnames = StringVar(value=pubnames)

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

lbl = ttk.Label(c, text="Papers                                                                                                                                                                                 ")
load = ttk.Button(c, text='Load', command=loadPubs, default='active')
save = ttk.Button(c, text='Save', command=savePubs, default='active')
lbox = Listbox(c, listvariable=pbnames, height=10)
lbl.grid(column = 0, row = 0, sticky=W)
lbox.grid(column = 0, row = 1, columnspan = 3, rowspan = 6, sticky = (N,S,E,W))
load.grid(column=1, row=0, sticky=E)
save.grid(column=2, row=0, sticky=E)
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)
root.mainloop()
