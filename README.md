# The Legend of Link - Projeto de Introdução a Programação
O grupo desenvolveu um sistema interativo 2D utilizando python e biblioteca Pygame. O jogo "The Link of Legend" tem como objetivo apenas a coleta de pedras preciosas como objetivo, contudo o game ainda será atualizado para receber inimigos magias dentre outros detalhes, porém será apresentado apenas a parte básica que já cumpre os requisitos solicitados do projeto.
#
# Imagem do game
![printjogo](https://user-images.githubusercontent.com/104574086/167874981-d42f2104-8ba5-4c7a-878d-0badba17a176.jpg)


# Grupo👷

* Matheus Fillipe Silva Malta - mfsm
* Newton Cardoso da Rocha Neto - ncrn
* Eduardo Dias de Oliveria Teles - edot
* Josef Jaeger Brandão - jjb
* Evandro de Souza Santos Junior - essj2
* Luiz Roberto Bezerra Ferreira - lrbf 

# Organização do Código
O projeto foi organizado seguindo a proposta de Orientação a Objetos ( POO ). A programação orientada a objetos propõe uma representação mais fácil de ser compreendida visualmente e para manutenção no código. Foram utilizadas duas classes, uma para o personagem jogável, e outra para os objetos coletados. Dentro no código 'main', chamado de 'jogobase', roda o loop principal do jogo e é onde ocorre todas as interações, como colisão e o relatório de coleta.

# Passos para rodar o jogo
É necessário apenas baixar o executável na branch 'main' e executá-lo em seu notebook. A movimentação do personagem consiste nas teclas W,A,S,D. Talvez o Windows não execute o arquivo imediatamente pois é de uma fonte desconhecida, porém é só clicar em executar mesmo assim.

# Ferramentas, Frameworks e Bibliotecas utilizadas 💻
* linguagem utilizada: Python
* Bibliotecas utilizadas para rodar o jogo: Pygame e Random. A Random foi utilizada para realizar o spawn aleatório dos objetos coletáveis.
* Ferramenta utilizada para criar os códigos: Pycharm

# Divisão do Trabalho✅
* Matheus Fillipe e Luiz Roberto: Realizaram a implementação do som do jogo, fontes de texto apresentados e a tela de menu.
* Eduardo Dias e Evandro de Souza: Realizaram a implementação do personagem, movimentação, animação e colisão com os outros objetos.
* Josef Jaeger e Newton Cardoso: Realizaram a implementação do fundo do jogo, assim como os obstáculos.

# Conceitos da Disciplina Utilizados:
* Condicionais -> Utilizamos operadores condicionais e lógicos praticamente no código inteiro, mas principalmente dentro do loop do jogo e do update do personagem, para fazer a movimentação do jogador e a sua interação com os objetos.
* Laços de Repetição -> Utilizamos o laços de repetição para executar o loop principal do jogo, para identificar se o jogo deve ser fechado e para gerar os spawns dos objetos coletáveis
* Listas -> Listas foram utilizadas na animação do personagem, onde foi criado uma lista com as imagens, e um laço de repetiçao as instanciam para que sejam exibidas num loop.
* Funções -> Foi utiliado uma função para executar o spawn dos objetos novamente depois que o jogo acaba e o usuário aperta para reiniciar.
* Módulos e Pacotes -> Utilizamos 3 módulos, um sendo o 'main', e outros dois para o personagem e os objetos. Assim, o código ficou mais organizado, e não misturou-se o código dos personagens e objetos com o resto do jogo.
* Orientação a Objetos -> Foi utilizado a orientação a objetos na criação do Personagem e dos ojetos coletados. Cada um em um módulo separado. Os objetos, como tem propriedades iguais são da mesma classe, e quando os 'chamamos', mudamos apenas as imagens.

# Desafios e lições:
- Desafios: A maior dificuldade encontrada pelo grupo foi a utilização do Github. Durante o desenvolvimento do projeto o grupo não utilizou o o diretório para compartilhar as alterações feitas no código, as vezes mandando por Discord ou por outras plataformas. Por causa disso, em alguns momentos houveram problemas pois o código era alterado ao ser enviado por aplicativos de comunicação comuns. Para contornar, o grupo procurou tutoriais de uso do github, e entegrantes da equipe que tinham mais familiriadade com a plataforma, ajudaram os outros.
Além disso, a equipe teve dificuldades para aprender a utilizar a biblioteca pygame no pouco tempo fornecido, assim, mecânicas que pretendíamos adicionar, como ataque, inimigos que atacariam o personagem e outros níveis não foram adicionadas.
- Lições: Com o projeto, aprendemos que definir bem as funções de cada integrante aumenta muito a eficiência do grupo. Também, como é importante ter um bom controle dos códigos e as alterações feitas por cada integrante, para não perder tempo tentando entender o que foi alterado no seu próprio código.
