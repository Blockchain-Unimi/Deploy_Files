from brownie import *
import json
import os


def abi_and_address (abi,address, name):
    """
    This function is to print abi and address of a contract
    into two files.txt. This is useful in order to upload
    contracts from abi during the challenge.
    """
    pretty_json = json.dumps(abi, indent=4)
    f = open(name+"_abi.txt", "w")
    f.write(pretty_json)
    f.close()
    f = open(name+"_address.txt", "w")
    f.write((address))
    f.close()
    

"""
Questo script è per il deploy dei paycoins. Solo uno di noi dovrà
lanciarlo. Il deploy dei paycoin viene eseguito da un unico account
che nel mio locale ho chiamato "Paycoin_admin". Su Metamask puoi
vedere la chiave privata. Nel mio locale, la pw è "TheBigFive".

Questo script oltre a fare il deploy consente di mintare i paycoins
a tutti i giocatori. Chiaramente per farlo devi caricare l'account
da locale. Quindi chi lancerà lo script dovrà aver impostato nel
suo locale tutti e cinque i wallets, per caricarli per il minting
in questo script.

viene scritto in due file.txt l'address e l'abi del paycoin.
"""
  
p=project.load("/Users/riccardobeccaria/Desktop/Magistrale/Metodi_Comput/Block_chain/Esame", name ="TokenProject")

from brownie.project.TokenProject import Token, Pool, TimeMarket, Challenge
p.load_config()

network.connect('ropsten')
#network.connect('development')

paycoin_mnemonic = "black sense blind capital trust idea century praise recipe live end miss"

paycoin_admin = accounts.from_mnemonic(paycoin_mnemonic)

becca_wallet = '0x4f6374606526BC5892D5C3037cE68da5712B4Efe'
citte_wallet = '0xebf84b5aa7a66412863F8F66655B5876EF92d91F'
pacio_wallet = '0xc89304bE60b1184281cDacF8e9ADD215B960Fcb8'
diana_wallet = '0x0B3DE044dC8b2902e6B668Cc43bfedB39dfA8fcD'
fra_wallet = '0x66F26b71404A133F4e478Fb5f52a8105fB324F6e'

paycoin = paycoin_admin.deploy(Token, "Paycoins", "Pay", 18)

paycoin.mint(becca_wallet, 50000*(10**paycoin.decimals()), {'from':paycoin_admin})
paycoin.mint(citte_wallet, 50000*(10**paycoin.decimals()), {'from':paycoin_admin})
paycoin.mint(pacio_wallet, 50000*(10**paycoin.decimals()), {'from':paycoin_admin})
paycoin.mint(diana_wallet, 50000*(10**paycoin.decimals()), {'from':paycoin_admin})
paycoin.mint(fra_wallet, 50000*(10**paycoin.decimals()), {'from':paycoin_admin})

challenge = Challenge.deploy(paycoin.address, [becca_wallet, citte_wallet, pacio_wallet, diana_wallet, fra_wallet], {'from':paycoin_admin})


abi_and_address (paycoin.abi,paycoin.address, "paycoin")
abi_and_address (challenge.abi, challenge.address, "challenge")

os.system("mv *.txt abi")
