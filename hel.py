from tkinter import filedialog
from tkinter import *
import json
import bibprint


root = Tk()
name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes= (("json files","*.json"),("all files","*.*")))
print(name)
s = ""
with open(name) as f:
    s = f.read();

#print(s)
parsed = json.loads(s)
#print(parsed)
contrs = parsed['contributions']
i = 57
for contr in contrs:
    i = i + 1
    #prn = bibprint.printForDissSovetRinc(contr, i)
    # prn = bibprint.printForDissSovetBases(contr, i)
#    bibprint.printForMiet(contr, i)
    prn = bibprint.printForGost(contr, i)
    #bibprint.printJSON(contr)
    if prn:
        print(prn)

#for aut in auth:
#    fst = aut['1st']
#    snd = aut['2nd']
#    print(fst[0] + ". " + snd)
#weird_json = '{"x": 1, "y": 2, "z": 3}'
#json.loads(weird_json)

