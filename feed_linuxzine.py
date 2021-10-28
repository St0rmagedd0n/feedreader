!/usr/bin/python3

import feedparser
import ssl
import json
import time

def trasformo_mese(mese):
    switcher={ 
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'}
    return switcher.get(mese,"Mese errato")

def ordina(e):
    return e['published']

with open('feed.json') as fonte:
    siti = json.load(fonte)


data = []

for i in range(len(siti)):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    rss = feedparser.parse(siti[i]['url'])
	try:
        print("Leggo: "+rss.feed.title+" per "+str(len(rss['entries']))+ " elementi")
        for j in range(len(rss['entries'])):
            try:
                feed_title = rss.feed.title
                published = rss['entries'][j]['published']
                anno_p = str(published[12:16])
                mese_p = str(published[8:11])
                mese_p = trasformo_mese(mese_p)
                giorno_p = str(published[5:7])
                ora_p = str(published[17:19])
                minuto_p = str(published[20:22])
                pubblicato = anno_p + "/" + mese_p + "/" + giorno_p + "-"+ ora_p +":"+minuto_p
                if (mese_p == "Mese errato"):
                    pubblicato = time.strftime("%Y/%m/%d-08:00")
                title = rss['entries'][j]['title']
                summary = rss['entries'][j]['summary']
                link = rss['entries'][j]['link']
                data.append ({'feed' : feed_title, 'published': pubblicato,
				            'title': title, 'summary': summary, 'link': link })
            except:
                print("Errore generico")
    except:
        print("Non riesco a leggere il feed")

fonte.close()
data.sort(reverse = True, key=ordina)

dati_json = json.dumps(data, indent=4, sort_keys=True)

with open('feed_exit.json', 'w', encoding='utf8') as f_exit:
    f_exit.write(dati_json)


print()
print("Ho letto i feed e creato il file di uscita")
