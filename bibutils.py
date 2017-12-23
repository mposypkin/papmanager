import bibtags
from transliterate import translit, get_available_language_codes

def initRecord ():
    return {bibtags.doi : '', bibtags.type: '', bibtags.language : '', bibtags.year: '', bibtags.where : '', bibtags.title : '', bibtags.authors : [], bibtags.volume : '', bibtags.number : '',
                bibtags.pages : [], bibtags.url : '', bibtags.bases : [], bibtags.file : '', bibtags.id : ''}


def generatePaperId(jdict):
    papid = jdict[bibtags.year]
    for aut in jdict[bibtags.authors]:
        authsnd = translit(aut[bibtags.snd], 'ru', reversed=True)
        papid = papid + authsnd[0]
    tit = translit(jdict[bibtags.title], 'ru', reversed=True).split(' ')
    for it in tit:
        papid = papid + it[0]
    wr = translit(jdict[bibtags.where], 'ru', reversed=True).split(' ')
    for it in wr:
        papid = papid + it[0]
    return papid