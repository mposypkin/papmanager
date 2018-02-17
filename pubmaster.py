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

data = {'paperlist' : []}
state = {'cursel' : -1}

def loadPubs():
    name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(("json files", "*.json"), ("all files", "*.*")))
    lbl.config(text = name)
    with open(name) as f:
        s = f.read();
    lbox.delete(0, END)
    parsed = json.loads(s)
    contrs = parsed['contributions']
    data['paperlist'] = contrs
    i = 0
    for contr in contrs:
        lbox.insert(i, str(i + 1) + ". " + contr[bibtags.title])
        if i % 2 :
            lbox.itemconfigure(i, background='#f0f0ff')
        i = i + 1

def savePubs():
    print("Hello")

def getCurSelection():
    idxs = lbox.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        return idx
    else:
        print("NO SELECTION!!")
        return -1

def onSelect(*args):
    print("OnSelect")
    idx = getCurSelection()
    if(idx != -1):
        state['cursel'] = idx
        loadPub()

def loadPub():
    contrs = data['paperlist']
    idx = state['cursel']
    if(idx == -1):
        entry.delete(0, END)
        entry.insert(0, '')
    else:
        print(contrs[idx])
#        lbox.activate(idx)
        entry.delete(0, END)
        entry.insert(0, contrs[idx][bibtags.title])

def updatePub():
    contrs = data['paperlist']
    idx = state['cursel']
    name = entry.get()
    contrs[idx][bibtags.title] = name
    lbox.delete(idx)
    lbox.insert(idx, str(idx + 1) + '. ' + name)

pbnames = StringVar(value=pubnames)

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

lbl = ttk.Label(c, text="Papers", width = 100)
dummy = ttk.Label(c, text="")
load = ttk.Button(c, text='Load', command=loadPubs, default='active')
save = ttk.Button(c, text='Save', command=savePubs, default='active')
lbox = Listbox(c, listvariable=pbnames, height=10)
lbox.bind('<<ListboxSelect>>', onSelect)
entry = ttk.Entry(c, width = 100)
update = ttk.Button(c, text='Update', command=updatePub, default='active')

lbl.grid(column = 0, row = 0, sticky=W)
lbox.grid(column = 0, row = 1, columnspan = 3, rowspan = 6, sticky = (N,S,E,W))
load.grid(column=1, row=0, sticky=E)
save.grid(column=2, row=0, sticky=E)
dummy.grid(column=0, row = 9, sticky=W)
entry.grid(column=0, row = 10, sticky=W)
update.grid(column=2, row = 10, sticky=E)

c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)
root.mainloop()
