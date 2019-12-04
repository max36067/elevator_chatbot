import json

with open('cb/item.json','r') as it:
    data = json.load(it)
    data['wallpaper'] = 'true'
    data['key_1'] = 'true'
with open('cb/item.json','w') as it:
    json.dump(data,it,indent=2)