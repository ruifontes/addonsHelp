# Add-ons documentation #

## Informazioni ##
* Autori: Rui Fontes, Ângelo Abrantes, Zougane, Remy, Abdel e collaborazione di James Scholes
* Aggiornato il 05/03/2023
* Download [stable version][1]
* Compatibilità: NVDA 2017.2 e versioni successive


## Presentazione ##
Questo componente aggiuntivo fornisce un modo rapido per accedere alla documentazione per i componenti aggiuntivi installati. Verranno creati, nel menu Aiuto di NVDA, due sottomenu. Uno, chiamato \"Documentazione dei componenti aggiuntivi in esecuzione\", raggruppa la documentazione per ciascun componente aggiuntivo e rende disponibile un elenco di comandi per tutti gli addon in esecuzione, con una tabella per ciascun componente aggiuntivo. L'altro sottomenu si chiama \"Documentazione dei componenti aggiuntivi disabilitati\", elenca i componenti aggiuntivi disabilitati, dando accesso alla relativa documentazione. Si ricorda che i componenti aggiuntivi dei driver di sintesi vocale e display braille non appariranno in nessuna delle categorie precedenti. Si noti che è anche possibile accedere alla documentazione dei componenti aggiuntivi tramite il gestore dei componenti aggiuntivi di NVDA, menu Strumenti. Qui ci sono anche le informazioni sullo stato di un componente aggiuntivo. Ricorda inoltre che puoi accedere ai comandi di NVDA e dei componenti aggiuntivi nella finestra di dialogo Gestisci input. Tuttavia, in questa finestra di dialogo i comandi dei componenti aggiuntivi non sono raggruppati e non è possibile trovare un comando contenente \"windows\", per esempio ...

## Novità ##

### Versione 2022.03 ###
* Adattamento a NVDA 2022.1

### Versione 21.05 ###
*Adattamento a NVDA 2021.1

### Versione 2.1 ###
* Adattamento a NVDA 2019.3

### Versione 2.0 ###
* Ora, il componente aggiuntivo crea due menu nel menu Aiuto di NVDA.
* Nel menu \"documentazione componenti aggiuntivi in esecuzione\" è stata aggiunta un'opzione per visualizzare l'elenco comandi per gli * addon che verranno presentati in una tabella.
* Il menu \"Documentazione dei componenti aggiuntivi disabilitati\" raggruppa solo i componenti aggiuntivi disabilitati con i file della documentazione.
* Si noti che eventuali componenti aggiuntivi per display braille o sintesi vocali non verrano mai elencati qui.
* I componenti aggiuntivi vengono ora rappresentati dal riassunto e non dal nome.
* Miglioramenti nel codice.

### Versione 1.2 ###
* Risolti piccoli problemi;
* Risolta l'importazione del sottomenu nome dal riassunto del componente aggiuntivo;
* La documentazione verrà aperta nel browser predefinito, possibilmente in una nuova finestra.

### Versione 1.1 ###
* Compatibilità con Python3;
* Nuovo metodo per aggiungere sotto menu;
* Modificato il nome degli elementi del menu al riassunto del componente aggiuntivo, affinché i nomi dei menu siano, quando possibile, nella lingua dell'interfaccia.

### Versione 1.0 ###
* Versione iniziale di Zougane, Remy e Abdel aggiornata per essere compatibile con NVDA 2019.1.

[1]: https://addons.nvda-project.org/files/get.php?file=addonshelp
