import re
import sys
import json

enp = re.compile("(%.)\s(.*)")
jsondict = {'type': '', 'lang' : '', 'year': '', 'where': '', 'title': '', 'authors': [], 'volume': '', 'number': '',
                'pages': [], 'url': '', 'bases': []}
for line in sys.stdin:
    m = enp.match(line)
    if(m):
            tag = m.group(1)
            val = m.group(2)
            if(tag == "%0"):
                jsondict['type'] = val
            elif(tag == '%T'):
                jsondict['title'] = val
                if(re.match(".*[а-я].*", val)):
                    jsondict['lang'] = 'ru'
                else:
                    jsondict['lang'] = 'en'
            elif(tag == '%J'):
                jsondict['where'] = val
            elif (tag == '%B'):
                jsondict['where'] = val
            elif(tag == "%A"):
                am = re.match('(\S+),\s*(\S.*\S)', val)
                if((am.group(1) == 'Посыпкин') or (am.group(1) == 'Posypkin')):
                    jsondict['authors'].append({'1st': am.group(2), '2nd': am.group(1), 'me' : 'yes'})
                else:
                    jsondict['authors'].append({'1st': am.group(2), '2nd': am.group(1)})
            elif(tag == "%D"):
                jsondict['year'] = val
            elif(tag == '%P'):
                pm = re.match('(\d+)-(\d+)', val)
                jsondict['pages'] = [pm.group(1), pm.group(2)]
            elif (tag == '%V'):
                jsondict['volume'] = val
            elif(tag == '%N'):
                jsondict['number'] = val
            else:
                continue
    else:
        print(json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=4)+',')
        jsondict = {'type': '', 'lang' : '', 'year': '', 'where': '', 'title': '', 'authors': [], 'volume': '', 'number': '',
                'pages': [], 'url': '', 'bases': []}
#        print(jsondict)

#print(json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=4)+',')

