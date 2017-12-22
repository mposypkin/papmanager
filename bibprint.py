import bibtags
import re

def printForMiet(contr, i):
    print(i, end = "\t")
    title = contr['title']
    print(title, end = "\t")
    print("печ.", end="\t")
    where =  contr[bibtags.where]
    print(where, end=", ")
    year = contr[bibtags.year]
    print(year, end=", ")
    if(contr.get(bibtags.volume)):
        volume = contr[bibtags.volume]
        if(contr['lang'] == 'en'):
            print("vol. " + volume, end = ", ")
        else:
            print("Т. " +  volume, end = ", ")
    if(contr.get(bibtags.number)):
        number = contr[bibtags.number]
        if(contr['lang'] == 'en'):
            print("(" + number + ")", end = ", ")
        else:
            print("№ " +  number, end = ", ")
    pages = contr[bibtags.pages]
    if(contr[bibtags.language] == 'en'):
        print("pp. " + pages[0] + "-" + pages[1], end = "\t")
    else:
        print("C. " + pages[0] + "-" + pages[1], end="\t")
    print(int(pages[1])-int(pages[0]) + 1, end="\t")
    authors = contr[bibtags.authors]
    for j in range(len(authors)):
        author = authors[j]
        me = author.get(bibtags.me)
        if(me != 'yes'):
            fst = author[bibtags.fst]
            scn = author[bibtags.snd]
            prn = scn
            prn += ' '
            aum = re.match('(\S+)+', fst)
            grp = aum.groups()
            print(grp, ":")
            print(prn, end="")
            if(j != (len(authors) - 1)):
                print(", ", end="")

    return


def printForGost(contr, i):
    sep = ' - '
    prn = ""
    authors = contr[bibtags.authors]
    for j in range(len(authors)):
        author = authors[j]
        fst = author[bibtags.fst]
        scn = author[bibtags.snd]
        prn += scn
        prn += ' '
        aum = re.findall('\S+', fst)
        for nm in aum:
            prn += nm[0] + '.';
        if (j != (len(authors) - 1)):
            prn += ', ';
        else:
            prn += ' ';
    prn += contr[bibtags.title]
    prn += ' // '
    prn += contr[bibtags.where] + ". " + sep
    prn += contr[bibtags.year] + ". " + sep
    if (contr.get(bibtags.volume)):
        volume = contr[bibtags.volume]
        if (contr['lang'] == 'en'):
            prn += 'vol. ' + volume + '.' + sep
        else:
            prn += 'Т. ' + volume + '.' + sep
    if (contr.get(bibtags.number)):
        number = contr[bibtags.number]
        if (contr['lang'] == 'en'):
            prn += '(' + number + ')' + sep
        else:
            prn += '№ ' + number + '.' + sep
    pages = contr[bibtags.pages]
    if (contr[bibtags.language] == 'en'):
        prn += 'pp. ' + pages[0] + '-' + pages[1] + '.'
    else:
        prn += 'C. ' + pages[0] + "-" + pages[1] + '.'
    print(prn)
    return