# Dokumentation for tilføjelser #
## Information ##
* Forfattere: Rui Fontes, Ângelo Abrantes, Zougane, Remy, Abdel og i samarbejde med James Scholes
* Opdateret i 01/01/2024
* Download [stabil version][1]
* Kompatibilitet: Kompatibilitet: NVDA 2019.3 og senere


# Præsentation #
Denne tilføjelse giver dig hurtig adgang til dokumentation for de tilføjelsesprogrammer, du har installeret.  Det opretter to undermenuer i NVDA Help-menuen.  Det ene, kaldet \"Running add-ons documentation\", grupperer dokumentationen for hvert add-on og gør en liste over kommandoer for alle kørende add-ons tilgængelig, med en tabel for hvert add-on.  Den anden undermenu, kaldet \"Disabled add-ons documentation\", indeholder en liste over de deaktiverede add-ons og giver adgang til deres dokumentation.  Husk venligst, at Synth- og Braille-driver-tilføjelser ikke vises i nogen af de ovennævnte kategorier.  Bemærk, at du også kan få adgang til dokumentationen af tilføjelsesprogrammer via Add-ons manager i NVDA, menuen Værktøjer. Her har du også oplysninger om tilstanden af et add-on.  Husk også, at du kan få adgang til kommandoer for NVDA og add-ons i dialogboksen Input gestures (Indtastningsbevægelser). I denne dialog er add-ons-kommandoerne dog ikke grupperet, og du kan f.eks. ikke finde en kommando, der indeholder \"windows\"...


## Ændringer ##
### Version 2022.03 ###

### Version 21.05 ###

### Version 2.1 ###

### Version 2.0 ###
* Nu tilføjer pakken to menuer i NVDA-menuen under \"Hjælp\".
* Menuen \"dokumentation for kørende tilføjelser\" indeholder et menupunkt der viser en liste over kommandoer for de aktuelt kørende tilføjelsesprogrammer. Disse vises i en tabel.
* Menuen for dokumentation til deaktiverede tilføjelser grupperer kun de deaktiverede tilføjelser sammen med den tilhørende dokumentation.
* Bemærk at drivere tilføjet via tilføjelsespakker aldrig vises i ovennævnte menuer.
* Tilføjelsen er nu repræsenteret ved deres beskrivelse og ikke via deres navn.
* Nogle forbedringer i koden.

### Version 1.2 ###
* Rettet nogle små problemer;
*Rettet importering af navnet til undermenuer fra tilføjelsens beskrivelse;
* Tving dokumentation til at åbne i standardbrowseren, om muligt i et nyt vindue.

### Version 1.1 ###
# Kompatibilitet med Python 3;
# Ny måde at tilføje undermenuer på;
# Gjort det muligt at vise menupunkterne på det lokale sprog, hvis muligt;

### Version 1.0 ###
# Første udgivelse af Zougane, Remy og Abdel opdateret for at være kompatibel med NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2024.01.01/addonsHelp-2024.01.01.nvda-addon
