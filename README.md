# Deploy_Files

In questa repository viene postato tutto l'occorrente per il deploy iniziale da parte di ogni utente del proprio token e pool.

### Contenuto:

- `Bot_Minter_Data.json`: contiene l'indirizzo del bot minter e il suo mnemonic. Contiene inoltre l'indirizzo del contratto `Paycoin` di cui è Minter. WARNING: OGNUNO DOVRà GIRARE 0.2 ETH A QUESTO ACCOUNT PER TUTTI I DEPLOY E I MINTING
- `Starting_Pool_Ratios.json`: contiene la quantità iniziale di token e paycoin che andranno mintati alla pool di ciascuno. WARNING: DA AGGIUNGERE INDIRIZZI DI DIANA RICCARDO E FRANCESCO. DA CONCORDARE I RAPPORTI ESATTI.
- `initial_deploy.py`: script per effettuare il deploy. E' necessario che i due precedenti file si trovino nella stessa cartella di quest'ultimo per il funzionamento.
- `StartingPoolRatios_to_JSON.py`: script python che serve solamente per creare un JSON con i rapporti iniziali di liquidità che saranno presenti nelle pool di ciasscuno di noi.
- `addresses.json`: TEMPLATE del file .json che costruiremo una volta effettutato il deploy contenente tutte le informazioni pubbliche degli utenti e del bot minter.
- `addresses_TO_JSON.py`: prenderà tutti i file `YOURNAME_public_dict.json` che si vengono a creare dopo il deploy di ciascuno e costruisce in automatico il file `addresses.json`

### Istruzioni `initial_deploy.py`:

- Attendere il deploy iniziale del contratto Paycoin.
- Mettersi in un progetto brownie contente i contratti `Pool.sol`, `Faucet.sol`, `Token.sol` e con un valido `project_id token` di infura.
- Avere a portata di mano i `mnemonic` relativi sia al tuo account personale (ISTRUZIONI RETRIEVAL MNEMONIC) che al tuo account che userai per i bot.
- Lanciare il programma `initial_deploy.py`: verrà richiesto prima il mnemonic del tuo ACCOUNT PRIVATO, poi quello dell'ACCOUNT DEI BOT.
- Verrà richiesto un nome per il token, ad esempio "Ragublo" o "CitteCoin" (1 sola parola)
- Verrà richiesto un simbolo per il token, ad esempio "RgB" o "CtN", come convenzione potremmo tenere 3 lettere di cui solo quella centrale minuscola, le altre maiuscole.
- Verrà richiesto infine il tuo nome, ad esempio "Matteo". IMPORTANTE: scrivi il tuo nome (non soprannome) con la maiuscola. Servirà poi in un secondo script.
- In output riceverai due file. Il primo, `YOURNAME_public_dict.json` contiene il tuo indirizzo, l'indirizzo della tua pool e quello del tuo token. Devi uploadarlo in questa cartella e servirà per costruire il file totale con tutti gli indirizzi. Non modificarlo.
- Il secondo file, `private_dict.json` è PRIVATO, NON CONDIVIDERLO CON NESSUNO. Contiene il tuo indizzo personale e chiave privata (in termini di mnemonic), l'indirizzo del faucet di cui sei propiretario e che servirà per ricaricare in automatico i bot che fanno le transazioni,  l'indirizzo del
primo dei tuoi bot e la relativa chiave privata (in termini di mnemonic). Questo conservalo e copialo nelle cartello dove sono presenti script il cui funzionamento necessita di questo file (come, ad esempio, `running_bots.py`).


