
# Add-ons documentation #

## Informations ##
* Authors: Rui Fontes, Zougane, Remy, Abdel and colaboration of, among others, Ângelo Abrantes and James Scholes
* Updated in 26/12/2019
* Download [stable version][1]
* Compatibility: NVDA version 2017.2 to 2019.3

## Presentation ##
This add-on provides a quick way to access documentation for the add-ons you have installed.
It creates, in the NVDA Help menu, two  sub-menus.
One, called "Running add-ons documentation", groups the documentation for each add-on and make available  a list of commands for all running add-ons, with a table for each add-on.
The other sub-menu, called "Disabled add-ons documentation",  lists the disabled add-ons, gaving access to its documentation.
Please, remember that the Synth and Braille drivers add-ons will not appear in any of the above categories.

## Changes ##

### Version 2.1 ###
* Adaptation to NVDA 2019.3

### Version 2.0 ###
* Now, the add-on creates two menus in the NVDA Help menu.
* The "Running add-ons documentation" menu, have one more option to display the "List of commands for running add-ons", containing the commands for each add-on in a table.
* The "Disabled add-ons documentation" menu only group the disabled add-ons with documentation files.
* Note that Synth and Braille drivers add-ons never are listed in the above menus.
* The add-ons are now represented by their summary and not by their name.
* Some improvements in the code.

### Version 1.2 ###
* Small errors corrected;
* Name of submenu not imported from add-on summary;
* Force documentation to open in default browser, if possible in a new window.

### Version 1.1 ###
* Compatibility with Python 3;
* New way to add submenus;
* Changed the name of the menu itens to the summary addon to have the name of the menus in the language of the interface, when possible.

### Version 1.0 ###
* Initial release of Zougane, Remy and Abdel updated to be compatible with NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2.1/addonsHelp-2.1.nvda-addon
