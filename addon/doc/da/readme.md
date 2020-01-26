# Dokumentation for tilføjelser #

## Information ##
* Forfattere: Rui Fontes, Zougane, Remy, Abdel og yderligere samarbejdere blandt andet Ângelo Abrantes og James Scholes
* Opdateret 26/12/2019
* Download [stabil version][1]
* Kompatibilitet: NVDA 2017.3 til 2019.3

## Præsentation ##
Denne tilføjelse giver dig hurtig adgang til dokumentation for de tilføjelser, du har installeret.
Denne tilføjelse opretter to yderligere menupunkter i NVDA-menuen under "Hjælp". Den ene menu, der hedder "Dokumentation for kørende tilføjelser", grupperer dokumentationen for hver tilføjelse og stiller en liste over kommandoer til rådighed for alle kørende tilføjelsespakker.
Den anden undermenu kaldes "Dokumentation for deaktiverede tilføjelser", viser deaktiverede tilføjelser i en liste, som giver adgang til dokumentationen.
Husk, at drivere til punktdisplays og talesynteser der er tilføjet via tilføjelsespakker ikke vises i nogen af ovenstående kategorier. Bemærk, at du også kan få adgang til dokumentationen for tilføjelserne via "Administrer tilføjelsesprogrammer" i NVDA-menuen Værktøjer.
Her vil du også få oplyst om tilføjelsesprogrammer kører eller er deaktiverede. Husk også, at du kan få adgang til kommandoer for NVDA og dine installerede tilføjelser.
I denne dialog er de tildelte kommandoer imidlertid ikke grupperet, og du kan for eksempel ikke finde en kommando indeholdende "windows".

## Ændringer ##

###  2.1 ###
* Tilpasning til NVDA 2019.3

### Version 2.0 ###
* Nu tilføjer pakken to menuer i NVDA-menuen under "Hjælp".
* Menuen "dokumentation for kørende tilføjelser" indeholder et menupunkt der viser en liste over kommandoer for de aktuelt kørende tilføjelsesprogrammer. Disse vises i en tabel.
* Menuen for dokumentation til deaktiverede tilføjelser grupperer kun de deaktiverede tilføjelser sammen med den tilhørende dokumentation.
* Bemærk at drivere tilføjet via tilføjelsespakker aldrig vises i ovennævnte menuer.
* Tilføjelsen er nu repræsenteret ved deres beskrivelse og ikke via deres navn.
* Nogle forbedringer i koden.

### Version 1.2 ###
* Rettet nogle små problemer;
* Rettet importering af navnet til undermenuer fra tilføjelsens beskrivelse;
* Tving dokumentation til at åbne i standardbrowseren, om muligt i et nyt vindue.

### Version 1.1 ###
* Kompatibilitet med Python 3;
* Ny måde at tilføje undermenuer på;
* Gjort det muligt at vise menupunkterne på det lokale sprog, hvis muligt.

### Version 1.0 ###
* Første udgivelse af Zougane, Remy og Abdel opdateret for at være kompatibel med NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2.1/addonsHelp-2.1.nvda-addon
