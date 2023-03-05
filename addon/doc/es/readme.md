# Documentación de complementos #

## Información ##
* Autores: Rui Fontes, Ângelo Abrantes, Zougane, Rémy, Abdel, con la colaboración de James Scholes entre otros
* Actualizado el 05/03/2023
* Descargar [versión estable][1]
* Compatibilidad con NVDA: 2017.3 y más allá

## Presentación ##
Este complemento proporciona una manera rápida de acceder a la documentación de los complementos que tengas instalados.
Para ello crea, en el menú Ayuda de NVDA, dos submenús.
Uno, llamado "Documentación de complementos en ejecución", agrupa la documentación de cada complemento y proporciona una lista de órdenes de todos los complementos disponibles en ejecución, con una tabla para cada uno.
Otro submenú llamado "Documentación de complementos deshabilitados", lista los complementos deshabilitados, dando acceso a su documentación.
Por favor, ten en cuenta que los controladores de síntesis de voz y pantallas braille no se mostrarán en estas categorías.
Ten en cuenta que también puedes acceder a la documentación de los complementos mediante el administrador de complementos en el menú herramientas de NVDA. Allí también se encuentra información sobre el estado de cada complemento.
No olvides que también puedes acceder a las órdenes de NVDA y los complementos desde el diálogo Gestos de entrada. Sin embargo, en este diálogo las órdenes de los complementos no se agrupan y no puedes encontrar una orden con la palabra "Windows", por ejemplo...

## Cambios ##

### Versión 21.05 ###
* Adaptación a NVDA 2021.1

### Versión 2.1 ###
* Adaptación a NVDA 2019.3

### Versión 2.0 ###
* Ahora el complemento crea dos submenús en el menú Ayuda de NVDA.
* El menú "Documentación de complementos en ejecución" tiene una opción más para mostrar la "Lista de órdenes de complementos en ejecución", que contiene las órdenes de cada complemento en una tabla.
* El menú "Documentación de complementos deshabilitados" sólo agrupa los complementos deshabilitados con archivos de documentación.
* Ten en cuenta que los complementos de síntesis de voz y pantallas braille no se listan en estos menús.
* Los complementos ahora se representan mediante su descripción corta en vez de su nombre.
* Algunas mejoras en el código.

### Versión 1.2 ###
* Se han corregido pequeños errores;
* Corregida la importación del nombre del submenú desde la descripción corta del complemento;
* Se fuerza la apertura de la documentación en el navegador por defecto, en una nueva ventana si es posible.

### Versión 1.1 ###
* Compatibilidad con Python 3;
* Nueva forma de añadir submenús;
* Se ha cambiado el nombre de los elementos de menú para que coincida con la descripción corta del complemento, de tal forma que se traduzcan al idioma de la interfaz cuando sea posible.

### Versión 1.0 ###
* Versión inicial de Zougane, Remy y Abdel actualizada para ser compatible con NVDA 2019.1.

[1]: https://addons.nvda-project.org/files/get.php?file=addonshelp
