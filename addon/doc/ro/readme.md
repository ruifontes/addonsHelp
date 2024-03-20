# Add-ons documentation #

## Informații ##
* Autori: Rui Fontes, Ângelo Abrantes, Zougane, Remy, Abdel și colaboratori și James Scholes
* Actualizat pe 20/03/2024
* Descărcați [versiunea stabilă][1]
* Compatibilitate: NVDA 2019.3 și mai departe

## Prezentare ##
Acest supliment oferă o modalitate rapidă de accesare a documentației suplimentelor pe care le-ați instalat.
El creează, în meniul de ajutor al NVDA, două submeniuri.
Primul, numit „Documentația suplimentelor care rulează”, grupează documentația pentru fiecare supliment și face disponibilă o listă a comenzilor pentru toate suplimentele care rulează, cu câte un tabel pentru fiecare supliment.
Al doilea submeniu numit „Documentația suplimentelor dezactivate” listează suplimentele dezactivate, oferind acces la documentația sa.
Vă rugăm să țineți cont de faptul că suplimentele care au funcția de drivere pentru sintetizatoare și pentru afișaje braille nu vor apărea în niciuna dintre categoriile de mai sus.
Rețineți că puteți accesa documentația suplimentelor și din administratorul suplimentelor NVDA, aflat în meniul Instrumente. Aici găsiți și informații despre starea unui supliment.
De asemenea, rețineți că puteți accesa comenzile NVDA și ale suplimentelor sale din dialogul Gesturi de intrare. Totuși, În acest dialog, comenzile suplimentelor nu sunt grupate și nu puteți găsi o comandă care să conțină „windows” în mod implicit.

## Modificări ##

### Versiunea 21.05 ###
* Adaptation to NVDA 2021.1

### Versiunea 2.1 ###
* Adaptation to NVDA 2019.3

### Versiunea 2.0 ###
* Acum, suplimentul creează două submeniuri în meniul Ajutor din NVDA.
* Meniul documentației suplimentelor care rulează are încă o opțiune de afișare a listei de comenzi pentru suplimentele care rulează, conținând comenzile pentru fiecare supliment într-un tabel.
* Meniul documentației suplimentelor dezactivate grupează numai suplimentele dezactivate cu fișierele documentațiilor.
* Rețineți că driverele sintetizatoarelor și ale afișajelor braille nu sunt listate niciodată în meniurile de mai sus.
* Suplimentele sunt reprezentate de cuprins, nu de nume.
* Niște îmbunătățiri în cod.

### Versiunea 1.2 ###
* Mici defecte corectate;
* A fost reparat numele submeniul de importare din cuprinsul suplimentului;
* Documentația e forțată să se deschidă în browser-ul implicit, dacă e posibil într-o nouă fereastră.

### Versiunea 1.1 ###
* Compatibilitate cu Python 3;
* Un nou mod de a adăuga submeniuri;
* A fost modificat numele elementelor de meniu la cuprins supliment pentru ca numele meniurilor să fie în limba interfeței, dacă este posibil.

### Versiunea 1.0 ###
* Versiunea inițială de Zougane, Remy și Abdel actualizată să fie compatibilă cu NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2024.03.20/addonsHelp-2024.03.20.nvda-addon
