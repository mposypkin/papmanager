import bibtags
import bibutils
import re
import json
from transliterate import translit, get_available_language_codes

def printForDissSovetRinc(contr, i):
    if len(contr[bibtags.bases]) != 0 and contr[bibtags.bases][0] != bibtags.rinc:
        return None
    prn = contr[bibtags.year] + '\t'
    prnAuth = ''
    authors = contr[bibtags.authors]
    slist = True
    for j in range(len(authors)):
        author = authors[j]
        if slist:
            slist = False
        else:
            prnAuth += ', '
        fst = author[bibtags.fst]
        scn = author[bibtags.snd]
        prnAuth += scn
        prnAuth += ' '
        aum = re.findall('\S+', fst)
        for nm in aum:
           prnAuth += nm[0] + '.';
    prn += prnAuth + '\t'
    prn += contr[bibtags.title] + '\t'
    prn += contr[bibtags.where] + '\t'
    if contr.get(bibtags.volume):
        volume = contr[bibtags.volume]
        if(contr[bibtags.language] == bibtags.eng):
            prn += 'vol. ' + volume
        else:
            prn += 'Т. ' +  volume + ', '
        if contr.get(bibtags.number):
            number = contr[bibtags.number]
            if(contr[bibtags.language] == bibtags.eng):
                prn += '(' + number + ')' + ', '
            else:
                prn += '№ ' +  number + ', '
        else:
            if(contr[bibtags.language] == bibtags.eng):
                prn += ', '
    pages = contr[bibtags.pages]
    if contr[bibtags.language] == 'en':
        prn += 'pp. ' + pages[0] + '-' + pages[1] + '\t'
    else:
        prn += 'C. ' + pages[0] + '-' + pages[1] + '\t'
    prn += contr[bibtags.doi] + '\t'
    prn += '\t'
    prn += printForGost(contr, 0)
    return prn



def printForDissSovetBases(contr, i):
    if contr[bibtags.language] == bibtags.rus or len(contr[bibtags.bases]) == 0:
        return None
    prn = contr[bibtags.year] + '\t'
    prnAuth = ''
    authors = contr[bibtags.authors]
    slist = True
    for j in range(len(authors)):
        author = authors[j]
        if slist:
            slist = False
        else:
            prnAuth += ', '
        fst = author[bibtags.fst]
        scn = author[bibtags.snd]
        prnAuth += scn
        prnAuth += ' '
        aum = re.findall('\S+', fst)
        for nm in aum:
           prnAuth += nm[0] + '.';
    prn += prnAuth + '\t'
    prn += translit(prnAuth, 'ru', reversed = True) + '\t'
    prn += contr[bibtags.title] + '\t'
    prn += translit(contr[bibtags.title], 'ru', reversed = True) + '\t'
    prn += contr[bibtags.where] + '\t'
    if contr.get(bibtags.volume):
        volume = contr[bibtags.volume]
        if(contr[bibtags.language] == bibtags.eng):
            prn += 'vol. ' + volume
        else:
            prn += 'Т. ' +  volume + ', '
        if contr.get(bibtags.number):
            number = contr[bibtags.number]
            if(contr[bibtags.language] == bibtags.eng):
                prn += '(' + number + ')' + ', '
            else:
                prn += '№ ' +  number + ', '
        else:
            if(contr[bibtags.language] == bibtags.eng):
                prn += ', '
    pages = contr[bibtags.pages]
    if contr[bibtags.language] == 'en':
        prn += 'pp. ' + pages[0] + '-' + pages[1] + '\t'
    else:
        prn += 'C. ' + pages[0] + '-' + pages[1] + '\t'
    prn += contr[bibtags.doi] + '\t'
    prn += '\t'
    prn += printForGost(contr, 0)
    return prn

def printForMiet(contr, i):
    prn = '';
    prn += str(i) + '\t'
    prn += contr['title'] + '\t'
    prn += 'печ.' + '\t'
    prn += contr[bibtags.where] + ', ' + contr[bibtags.year] + ', '
    if contr.get(bibtags.volume):
        volume = contr[bibtags.volume]
        if(contr[bibtags.language] == bibtags.eng):
            prn += 'vol. ' + volume
        else:
            prn += 'Т. ' +  volume + ', '
    if contr.get(bibtags.number):
        number = contr[bibtags.number]
        if(contr[bibtags.language] == bibtags.eng):
            prn += '(' + number + ')' + ', '
        else:
            prn += '№ ' +  number + ', '
    pages = contr[bibtags.pages]
    if contr[bibtags.language] == 'en':
        prn += 'pp. ' + pages[0] + '-' + pages[1] + '\t'
    else:
        prn += 'C. ' + pages[0] + '-' + pages[1] + '\t'
    prn += str(int(pages[1])-int(pages[0]) + 1) + '\t'
    authors = contr[bibtags.authors]
    slist = True
    for j in range(len(authors)):
        author = authors[j]
        me = author.get(bibtags.me)
        if me != 'yes':
            if slist:
                slist = False
            else:
                prn += ', '
            fst = author[bibtags.fst]
            scn = author[bibtags.snd]
            prn += scn
            prn += ' '
            aum = re.findall('\S+', fst)
            for nm in aum:
                prn += nm[0] + '.';
    return prn


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
        if (contr[bibtags.language] == bibtags.eng):
            prn += 'vol. ' + volume
        else:
            prn += 'Т. ' + volume + '.' + sep
    if (contr.get(bibtags.number)):
        number = contr[bibtags.number]
        if (contr[bibtags.language] == bibtags.eng):
            prn += '(' + number + ')' + sep
        else:
            prn += '№ ' + number + '.' + sep
    pages = contr[bibtags.pages]
    if (contr[bibtags.language] == bibtags.eng):
        prn += 'pp. ' + pages[0] + '-' + pages[1] + '.'
    else:
        prn += 'C. ' + pages[0] + "-" + pages[1] + '.'
    return prn

def printJSON(contr):
    rec = bibutils.initRecord()
    for tag in rec.keys():
        if contr.get(tag):
            rec[tag] = contr[tag]
    rec[bibtags.id] = bibutils.generatePaperId(rec)
    print(json.dumps(rec, ensure_ascii=False, sort_keys=True, indent=4) + ',')