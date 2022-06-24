#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json

dizionario={}
names=['Matteo','Diana','Francesco','Riccardo','Cristiano']
botminterdata=json.loads(open('Bot_Minter_Data.json').read())

for name in names:

    to_append=json.loads(open(f'{name}_public_dict.json').read())
    dizionario[f'{name}']=to_append[f'{name}']

dizionario['bot_minter']=botminterdata['bot_minter']

with open('addresses.json','w') as outfile:
    json.dump(dizionario,outfile)