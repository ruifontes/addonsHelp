
# Add-ons documentation #

## Informations ##
* Authors: Rui Fontes, Zougane, Remy, Abdel and colaboration of, among others, Ângelo Abrantes and James Scholes
* Updated in 30/04/2019
* Download [stable version][1]
* Compatibility: NVDA 2017.3 to 2019.2

## Presentation ##
This add-on provides a quick way to access documentation for the add-ons you have installed.
It creates, in the NVDA Help menu, two  sub-menus.
One, called "Running add-ons documentation", groups the documentation for each add-on and make available  a list of commands for all running add-ons, with a table for each add-on.
Other sub-menu called "Disabled add-ons documentation",  lists the disabled add-ons, gaving access to its documentation.
Please, remember that the Synth and Braille drivers add-ons will not appear in any of the above categories.
Note that you also can access the add-ons documentation through the Add-ons manager in NVDA, Tools menu. Here you have also the information about the state of an add-on.
Also remember that you can access the NVDA and add-ons commands in the Input gestures dialog. However, in this dialog the add-ons commands are not grouped and you can not find a command containing "windows", by instance...

## Changes ##

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

[1]: https://github.com/ruifontes/addonsHelp/releases/download/1.2/addonsHelp-1.2.nvda-addon
