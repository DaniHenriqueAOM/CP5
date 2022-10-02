### ------------------------------------------    *-- Jogo da Velha - CP5 --* ------------------------------------------
### --------------------------------------------    *-- Funções do jogo --* --------------------------------------------

# Função   que   inicializa   o   tabuleiro,   isto   é, prepara o tabuleiro para a jogada.Os parâmetros e o retorno devem ser definidos pelo programador.
def inicializaTabuleiro():
    tabuleiro = []
    for i in range(3):
        tabuleiro.append([" ", " ", " "])
    return tabuleiro

# Função  que  imprime  o  tabuleiro  de  jogo  da velha  para  o  usuário.  Obviamente,  se  ele  já estiver  preenchido  com  X's  e  O's,  então  estes deverão ser impressos.Não  há  retorno.  Os  parâmetros  devem  ser definidos pelo  programador.
def imprimirTabuleiro(tabuleiro):
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i != 2:
            print("-----------")

# Função que imprime menu principal do jogo. Os parâmetros e o retorno devem ser definidos pelo programador.
def imprimeMenuPrincipal():
    print("Jogo da Velha")
    print("1 - Jogar Usuário vs Usuário\n2 - Jogar Usuário vs Computador (Fácil)\n3 - Jogar Usuário vs Computador (Difícil)\n4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        PjogadorX = 0
        PjogadorO = 0
        modoJogador(PjogadorX, PjogadorO)
    elif opcao == 2:
        PjogadorX = 0
        PjogadorO = 0
        modoFacil(PjogadorX, PjogadorO)
    elif opcao == 3:
        PjogadorX = 0
        PjogadorO = 0
        modoDificil(PjogadorX, PjogadorO)
    elif opcao == 4:
        print("Obrigado por jogar!\nEncerrando programa...")
        exit()

# Função  sem  parâmetros  lê  e  devolve  para  o usuário a coordenada da linha.
def lerLinha():
    linha = int(input("Digite a linha (1, 2 ou 3): "))
    return linha - 1

# Função  sem  parâmetros  lê  e  devolve  para  o usuário a coordenada da coluna.
def lerColuna():
    coluna = int(input("Digite a coluna (1, 2 ou 3): "))
    return coluna - 1

# Função que imprime o status do jogo, ou seja, a  pontuação  de  cada  jogador  na  partida  Essa função   deve   ser   chamada   diversas   vezes, sempre que iniciar um novo jogo.Não  há  retorno.  Os  parâmetros  devem  ser definidos pelo programador.
def imprimePontuacao(jogadorX, jogadorO):
    print(f"------------*Pontuação*------------\nJogador X: {jogadorX} x Jogador O: {jogadorO}")

# Função para inserir a pontuação do jogador no tabuleiro.
def inserirPontuacao(jogadorX, jogadorO):
    if jogadorX == True:
        PjogadorX += 1
    elif jogadorO == True:
        PjogadorO += 1
    return PjogadorX, PjogadorO

# Recebe   coordenadas   de   linha   e   coluna   e verifica se aquela posição é válida (ou seja, se ela   é   existente   no   tabuleiro   e   se   aquela posição está vazia).O retorno deve ser definido pelo programador. Sugestão: retornar um valor booleano. Observação:  se  preferir,  você pode  adicionar adicionais  além  das  coordenadas  de  linha  e coluna nessa função.
def posicaoValida(linha, coluna, tabuleiro):
    if linha not in range(3) or coluna not in range(3):
        print("Posição fora da Matriz! Digite novamente...")
        imprimirTabuleiro(tabuleiro)
        return False
    elif tabuleiro[linha][coluna] != " ":
        print("Posição já ocupada! Digite novamente...")
        imprimirTabuleiro(tabuleiro)
        return False
    elif tabuleiro[linha][coluna] == " ":
        return True

# Função para validar a posição do computador. ( intuito de não imprimir as mesmas informações que as do jogador )
def posicaoValidaComputador(linha, coluna, tabuleiro):
    if linha not in range(3) or coluna not in range(3):
        return False
    elif tabuleiro[linha][coluna] != " ":
        return False
    elif tabuleiro[linha][coluna] == " ":
        return True
    

# Função  que  verifica  se  houve  um  vencedor, seja ele o jogador 1, jogador 2 ou máquina.Os parâmetros e o retorno devem ser definidos pelo programador.
def verificaVencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            print(f"O jogador com {tabuleiro[i][0]} venceu!")
            return True
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
            print(f"O jogador com {tabuleiro[0][j]} venceu!")
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        print(f"O jogador com {tabuleiro[0][0]} venceu!")
        return True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        print(f"O jogador com {tabuleiro[2][0]} venceu!")
        return True
    else:
        return False

# Função  que  verifica  se  o  jogo  encerrou  em velha, isto é, empate.Os parâmetros e o retorno devem ser definidos pelo programador.
def verificaVelha(tabuleiro):
    contador = 0
    for i in tabuleiro:
        for j in i:
            if j != " ":
                contador += 1
    if contador == 9:
        print("O jogo empatou!")
        return True
    else:
        return False

# Função que realiza todas as operações para a opção de usuário-jogador vs. usuário-jogador.Os parâmetros e o retorno devem ser definidos pelo programador.
def modoJogador(PjogadorX, PjogadorO):
    tabuleiro = inicializaTabuleiro()
    jogadorX = "X"
    jogadorO = "O"
    aux = False
    imprimePontuacao(PjogadorX, PjogadorO)
    while aux == False:
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogadorX)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            PjogadorX += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogadorO)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            PjogadorO += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
    cond = input("Deseja jogar novamente? (S/N) ")
    if cond == "S" or cond == "s":

        modoJogador(PjogadorX, PjogadorO)
    else:
        print("\nObrigado por jogar!\nEncerrando programa...")
        return

# Função que realiza todas as operações para a opção de usuário-jogador vs. computador nível fácil.Os parâmetros e o retorno devem ser definidos pelo programador.
def modoFacil(PjogadorX, PjogadorO):
    tabuleiro = inicializaTabuleiro()
    jogadorX = "X"
    jogadorO = "O"
    aux = False
    imprimePontuacao(PjogadorX, PjogadorO)
    while aux == False:
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogadorX)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            PjogadorX += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
        imprimirTabuleiro(tabuleiro)
        print("Vez do computador...")
        jogadaFacil(tabuleiro)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            PjogadorO += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
    cond = input("Deseja jogar novamente? (S/N) ")
    if cond == "S" or cond == "s":

        modoFacil(PjogadorX, PjogadorO)
    else:
        print("\nObrigado por jogar!\nEncerrando programa...")
        return

# Função que realiza todas as operações para a opção de usuário-jogador vs. computador nível difícil.Os parâmetros e o retorno devem ser definidos pelo programador.
def modoDificil():
    pass

# Função que recebe as coordenadas de linha e coluna e preenche exclusivamente o tabuleiro. O  atribuição  no  tabuleiro  só  pode  ser  feito por esta função. Ela deverá ser usada pelos jogadores e pelo computador.A  função  jogada  apenas  atribui  "X"  ou  "O"  no tabuleiro. A validação da jogada (por exemplo, se  a  coordenada  é  válida  ou  não)  deve  ser feita em outra função. Observação:  se  preferir,  você pode  adicionar adicionais  além  das  coordenadas  de  linha  e coluna nessa função.O retorno deve ser definido pelo programador.
def jogar(linha, coluna, tabuleiro, XouO):
    tabuleiro[linha][coluna] = XouO

# Função   que   recebe   as   coordenadas   do jogador  e  obrigatoriamente  chama  a  função jogar para inserir no tabuleiro.O retorno deve ser definido pelo programador.
def jogadaUsuario(tabuleiro, XouO):
    print(f"Jogador {XouO} digite a linha e a coluna que deseja jogar:")
    linha = lerLinha()
    coluna = lerColuna()
    if posicaoValida(linha, coluna, tabuleiro) == True:
        jogar(linha, coluna, tabuleiro, XouO)
    else:
        jogadaUsuario(tabuleiro, XouO) # Caso a posição não seja válida, a função é chamada novamente

# Função   que   gera   coordenadas   de   linha   e colunas aleatórias e obrigatoriamente chama a função jogar para inserir no tabuleiro.O retorno deve ser definido pelo programador.
def jogadaFacil(tabuleiro):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicaoValidaComputador(linha, coluna, tabuleiro) == True:
            jogar(linha, coluna, tabuleiro, "O")
            break

# Função que calculará qual a melhor jogada de linha  e  coluna  e  obrigatoriamente  chama  a função jogar para inserir no tabuleiro. Para as regras,   veja   a   subseção:   "JOGADOR-USUÁRIO   CONTRA   A   MÁQUINA   -   NÍVEL DIFÍCIL"
def jogadaDificil(tabuleiro):
    pass

### -------------------------------------------  *-- Codigo Principal --*  ----------------------------------------------
import random
imprimeMenuPrincipal()
