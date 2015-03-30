Abaixo estão listados os softwares e bibliotecas que devem estar instalados antes de utilizar o rrt-planner.

## Softwares ##
  * [Python](http://www.python.org/download/)
  * Player/Stage - [Site oficial](http://playerstage.sourceforge.net/) - [Tutorial sobre instalação](http://www.control.aau.dk/~tb/wiki/index.php/Installing_Player_and_Stage_in_Ubuntu)

## Bibliotecas ##
  * [matplotlib](http://matplotlib.sourceforge.net)
  * [NumPy](http://numpy.scipy.org/)
  * [PIL](http://www.pythonware.com/products/pil/)
  * [python-graph](http://code.google.com/p/python-graph/)
  * Binding da libplayerc para Python - Em sistemas "apt-get" normalmente referenciada pelo nome python-playerc.

## Versões utilizadas no desenvolvimento ##
Para o desenvolvimento desse software está sendo utilizado a plataforma Kubuntu/Linux 9.04.
Para realizar a instalação, os códigos fonte foram obtidos do site do projeto Player/Stage [Onde obter o código fonte](http://sourceforge.net/projects/playerstage/files/)

Primeiro compile o player, seguindo as instruções do arquivo INSTALL. Certifique-se que as dependências lá citadas, estejam instaladas em sua máquina. Certifique-se também que a biblioteca libtool esteja instalada, pois senão o player não dará suporte a `shared objects`.
  * player - Version: 3.0.0-rc2
  * stage - Version: 3.1.0

Os demais pacotes (`matplotlib`, `NumPy`, `PIL`, `python-graph`) foram instalados utilizando-se a ferramenta `easy_install` ou pelo respectivo pacote pertencente a versão 9.04 do Kubuntu/Linux.