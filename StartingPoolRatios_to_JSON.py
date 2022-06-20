#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json

dizionario={

    'token':{
        '0xebf84b5aa7a66412863F8F66655B5876EF92d91F':100,           #Matteo
        '0x4f6374606526BC5892D5C3037cE68da5712B4Efe':1000,          #riccardo
        '0xc89304bE60b1184281cDacF8e9ADD215B960Fcb8':10000,         #Cristiano
        '0x0B3DE044dC8b2902e6B668Cc43bfedB39dfA8fcD':100000,        #Diana
        '0x66F26b71404A133F4e478Fb5f52a8105fB324F6e':10000000},     #Francesco

    'paycoin':{
        '0xebf84b5aa7a66412863F8F66655B5876EF92d91F':100000,         #Matteo
        '0x4f6374606526BC5892D5C3037cE68da5712B4Efe':100000,         #riccardo
        '0xc89304bE60b1184281cDacF8e9ADD215B960Fcb8':100000,         #Cristiano
        '0x0B3DE044dC8b2902e6B668Cc43bfedB39dfA8fcD':100000,         #Diana
        '0x66F26b71404A133F4e478Fb5f52a8105fB324F6e':100000,         #Francesco

    }
}

with open('Starting_Pool_Ratios.json','w') as outfile:
    json.dump(dizionario,outfile)