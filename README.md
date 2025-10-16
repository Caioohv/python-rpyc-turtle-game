# python-rpyc-turtle-game
Exercício proposto na disciplina de Sistemas Distribuídos

Enunciado:
Você foi contratado(a) para desenvolver a comunicação em um jogo de movimentação de bolas em um campo. A principal parte de jogabilidade já está pronta e disponível no código “game.py” no repositório do GitHub: https://github.com/Garrocho/sistemas_distribuidos/tree/main/objetos

Para testar o jogo, execute em um terminal o seguinte comando:

python3 game.py

Seu chefe está convicto que a melhor abordagem de comunicação nesse jogo distribuído é um estilo arquitetônico baseado em eventos. Assim, ele definiu as seguintes tarefas a serem seguidas:
Criar um servidor RPC que permita intermediar a comunicação entre todos os jogadores;
Cada jogador, deverá ter clientes RPC que:
após o jogador fazer um movimento, este movimento deve ser publicado no servidor RPC;
recebe os movimentos de todos os jogadores e atualiza a jogada em sua interface gráfica.
Cada jogador deve utilizar uma máquina física diferente, mas um servidor RPC pode estar executando em background em uma mesma máquina de um cliente (para simplificar o desenvolvimento);
Não há limitação de jogadores neste jogo.
