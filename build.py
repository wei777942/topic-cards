import json
d=json.load(open('decks.json',encoding='utf8'))
for x in d: assert len(x['cards'])==52 and len(set(x['cards']))==52,x['id']
open('index.html','w',encoding='utf8').write(open('template.html',encoding='utf8').read().replace('__DECKS__',json.dumps(d,ensure_ascii=False)))
