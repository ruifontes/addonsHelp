# Documentation des extensions #

## Informations ##
* Auteurs : Rui Fontes, Ângelo Abrantes, Zougane, Remy, Abdel et la collaboration de James Scholes
* Mis à jour le 20/03/2024
* Télécharger : [version stable][1]
* Compatibilité : NVDA 2019.3 et au-delà

## Présentation ##
Cette extension fournit un moyen rapide d'accéder à la documentation des extensions que vous avez installées.
Elle ajoute, dans le menu Aide de NVDA, deux sous-menus.
L'un, appelé "Documentation des extensions en cours d'exécution", regroupe la documentation de chaque extension et met à disposition une liste de commandes pour toutes les extensions en cours d'exécution, avec un tableau pour chaque extension.
L'autre sous-menu intitulé "Documentation des extensions désactivées" répertorie les extensions désactivées, donnant accès à leur documentation.
Notez que les synthétiseurs et pilotes Braille ajoutés n'apparaîtront dans aucune des catégories ci-dessus.
Notez que vous pouvez également accéder à la documentation des extensions par le biais du gestionnaire d'extensions dans NVDA, menu Outils. Ici, vous avez également les informations sur l'état d'une extension.
N'oubliez pas non plus que vous pouvez accéder aux commandes NVDA et à celles des extensions dans la boîte de dialogue Gestes de commandes. Cependant, dans cette boîte de dialogue, les commandes d’extensions ne sont pas groupées et vous ne pouvez pas trouver une commande contenant "windows", par exemple ...

## Changements ##

### Version 21.05 ###
* Adaptation à NVDA 2021.1

### Version 2.1 ###
* Adaptation à NVDA 2019.3

### Version 2.0 ###
* L'extension ajoute maintenant 2 sous-menus au menu Aide de NVDA.
* L'extension ajoute maintenant 2 sous-menus au menu Aide de NVDA.
* Le menu "Documentation des extensions désactivées" affiche uniquement la liste des fichiers de documentation des extensions inactives.
* Notez bien que les synthétiseurs et pilotes Braille ne sont pas affichés dans les menus ci-dessus.
* Les extensions sont maintenant présentées par leur description et non plus par leur nom.
* Quelques améliorations du code.

### Version 1.2 ###
* Corrections mineures;
* Le nom des sous-menus n'est plus importé depuis la description des extensions;
* La documentation s'ouvrira maintenant dans le navigateur par défaut, dans une nouvelle fenêtre si possible.

### Version 1.1 ###
* Compatibilité avec Python 3;
* Nouvelle manière d'ajouter des sous-menus;
* Changement des noms des éléments de menus, ils se basent maintenant sur la description des extensions, cela permet d'avoir le nom des menus dans la langue de l'interface, quand c'est possible.

### Version 1.0 ###
* Première version par Abdel, Zougane et Remy, mise à jour pour être compatible avec NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2024.03.20/addonsHelp-2024.03.20.nvda-addon
