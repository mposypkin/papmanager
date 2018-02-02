import re
import sys
import json
import bibtags
import bibutils

def convertType(val):
    if(re.match('.*[Jj]ournal.*', val)):
        return bibtags.journal
    elif(re.match('.*[Pp]roceedings.*', val)):
        return  bibtags.proceedings
    else:
        return bibtags.book


enp = re.compile("(%.)\s(.*)")
jsondict = bibutils.initRecord()

for line in sys.stdin:
    m = enp.match(line)
    if(m):
            tag = m.group(1)
            val = m.group(2)
            if(tag == "%0"):
                jsondict[bibtags.type] = convertType(val)
            elif(tag == '%T'):
                jsondict[bibtags.title] = val.capitalize().strip()
                if(re.match(".*[а-я].*", jsondict[bibtags.title])):
                    jsondict[bibtags.language] = bibtags.rus
                else:
                    jsondict[bibtags.language] = bibtags.eng
            elif(tag == '%J'):
                jsondict[bibtags.where] = val.strip()
            elif (tag == '%I'):
                jsondict[bibtags.publisher] = val
            elif (tag == '%B'):
                jsondict[bibtags.where] = val
            elif(tag == "%A"):
                am = re.match('(\S+),\s*(\S+)', val)
                #if((am.group(1) == 'Посыпкин') or (am.group(1) == 'Posypkin')):
                if (bibtags.mynames.count(am.group(1)) > 0):
                    jsondict[bibtags.authors].append({bibtags.fst: am.group(2), bibtags.snd: am.group(1), bibtags.me : bibtags.yes})
                else:
                    jsondict[bibtags.authors].append({bibtags.fst: am.group(2), bibtags.snd: am.group(1)})
            elif(tag == "%D"):
                jsondict[bibtags.year] = val
            elif(tag == '%P'):
                pm = re.match('(\d+)-(\d+)', val)
                jsondict[bibtags.pages] = [pm.group(1), pm.group(2)]
            elif (tag == '%V'):
                jsondict[bibtags.volume] = val
            elif(tag == '%N'):
                jsondict[bibtags.number] = val
            else:
                continue
    else:
        jsondict[bibtags.id] = bibutils.generatePaperId(jsondict)
        print(json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=4)+',')
        jsondict = bibutils.initRecord()

        #jsondict = {'type': '', 'lang' : '', 'year': '', 'where': '', 'title': '', 'authors': [], 'volume': '', 'number': '',
#                'pages': [], 'url': '', 'bases': []}
#        print(jsondict)

#print(json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=4)+',')

