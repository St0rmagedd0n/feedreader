#!/usr/bin/python3

import json

with open('feed_exit.json') as fonte:
    input = json.load(fonte)

data = ""

data = data+"---\n"
data = data+"title: Feed News\n"
data = data+"---\n"
data = data+"\n"
data = data+"# Feed News\n"

for i in range(len(input)):
    nome = input[i]['feed']
    titolo = input[i]['title']
    contenuto = input[i]['summary']
    data_pub = input[i]['published']
    link = input[i]['link']
    data = data+"\n## "+titolo+" - "+nome+" ("+data_pub+")\n"
    data = data+"\n"
    data = data+contenuto+"\n\n"
    data = data+"["+link+"]("+link+")\n"

#print(data)

with open('default.md', 'w', encoding='utf8') as f_exit:
    f_exit.write(str(data))