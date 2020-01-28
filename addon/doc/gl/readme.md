# Documentación de complementos #

## Información ##
* Autores: Rui Fontes, Zougane, Remy, Abdel e colaboracións, entre outras, de Ângelo Abrantes e James Scholes
* Actualizado o 26/12/2019
* Descargar [versión estable][1]
* compatibilidade: de NVDA 2017.3 a 2019.3

## Presentación ##
Este complemento proporciona un método rápido para acceder á documentación dos complementos que tes instalados. 
Crea, no menú Axuda de NVDA, dous submenús. 
Un, chamado "Documentación de complementos en execución", agrupa a documentación para cada complemento e subministra unha listaxe de atallos para todos os complementos en execución, cunha táboa para cada complemento. 
Outro submenú chamado "Documentación de complementos deshabilitados", lista os complementos deshabilitados, dando acceso á súa documentación. 
Por favor, lembra que os complementos de controladores de sintetizadores e braille non aparecerán en ningunha das categorías de enriba. 
Ten en conta que tamén podes acceder á documentación dos complementos a través do Administrador de complementos no menú NVDA, Ferramentas. Alí tamén tes a información sobre o estado dun complemento. 
Lembra tamén que podes acceder aos atallos do NVDA e os complementos no diálogo Xestos de entrada. Porén, neste diálogo os atallos de complementos non están agrupados e non podes encontrar un atallo que conteña "xanelas", por exemplo.

## Cambios ##

### Versión 2.1 ###
* Adaptación ó NVDA 2019.3

### Versión 2.0 ###
* Agora, o complemento crea dous menús no menú Axuda de NVDA.
* O menú "documentación de complementos en execución" ten unha opción máis, para amosar a "Listaxe de atallos de complementos en execución", que contén os atallos de cada complemento nunha táboa 
* O menú "documentación de complementos deshabilitados" só agrupa ós complementos deshabilitados con arquivos de documentación.
* Ten en conta que os complementos de controladores de sintetizadores e braille nunca se listan nos menús de enriba.
* Os complementos represéntanse polo seu resumo e non polo seu nome.
* Algunhas melloras no código.

### Versión 1.2 ###
* Arranxadas pequenas incidencias;
* Arranxada a importación do nome do submenú dende o resumo do complemento;
* forzar documentación a abrirse no navegador predeterminado, nunha nova xanela se é posible.

### Versión 1.1 ###
* compatibilidade con Python 3;
* Novo método para engadir submenús;
* Cambiado o nome dos elementos de menú ao resumo do complemento, para ter os nomes dos menús na lingua da interface, cando sexa posible.

### Versión 1.0 ###
* Versión inicial de Zougane, Rémy e Abdel actualizada para que sexa compatible con NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2.1.0/addonsHelp-2.1.nvda-addon
