# Documentação dos extras #

## Informações ##
* Autores: Rui Fontes, Ângelo Abrantes, Zougane and Rémy, Abdel com colaboração de James Scholles
* actualizado em 20/03/2024
* Descarregar a [versão estável][1]
* Compatibilidade: NVDA versão 2019.3 e seguintes

# Apresentação #
Este complemento fornece uma maneira rápida de acessar a documentação dos complementos que você instalou.
Cria, no menu Ajuda do NVDA, dois submenus.
Um, chamado "Documentação dos extras em execução", agrupa a documentação para cada complemento e disponibiliza uma lista de comandos para todos os extras em execução, com uma tabela para cada extra.
Outro submenu, chamado "Documentação dos extras desactivados", lista os extras desativados, permitindo acesso à sua documentação.
Lembre-se que os extras dos drivers de Sintetizadores  e de linhas Braille não aparecerão em nenhuma das categorias acima.
Note que também pode aceder à documentação dos extras através do "Gestor de extras", menu do NVDA, Ferramentas. Aqui também encontrará informação sobre o estado de cada extra.
Lembre-se que também pode aceder aos comandos do NVDA e dos extras no diálogo "Definir comandos". No entanto, neste diálogo os comandos não estão agrupados por extras e não pode pesquisar por um comando contendo a tecla "windows", por exemplo ...

## Alterações ##

### Versão 21.05 ###
* Adaptação para NVDA 2021.1

### Versão 2.1 ###
* Adaptação para NVDA 2019.3

### Versão 2.0 ###
* Agora, o extra cria dois menus no menu Ajuda do NVDA;
* O menu "Documentação dos extras em execução", tem mais uma opção para disponibilizar uma "Lista de comandos para os extras em execução", contendo os comandos para cada extra  numa tabela;
* O menu "Documentação dos extras desactivados" apenas agrupa a documentação para cada extra desactivado contendo documentação;
* Note que os extras dos drivers de Sintetizadores  e de linhas Braille não aparecerão em nenhuma das categorias acima;
* Os extras passam a ser designados pelo sumário, en vez do nome;
* Algumas melhorias no código.

### Versão 1.2 ###
* Correcção de pequenos erros;
* Nome do submenu já não é importado do "summary" do extra;
* Forçar a documentação a abrir no navegador padrão, se possível numa nova janela.

### Versão 1.1 ###
* Compatibilidade com Python 3;
*	 Nova maneira de adicionar os submenus;
* Alterado o nome dos menus para o sumário dos mesmos para se ter o nome dos menus na língua da interface, quando possível.

### Versão 1.0 ###
*	 Versão inicial de Zougane, Rémy e Abdel actualizada para ser compatível com NVDA 2019.1.

[1]: https://github.com/ruifontes/addonsHelp/releases/download/2024.03.20/addonsHelp-2024.03.20.nvda-addon
