#113) (matriz) Crie um programa que armazene a pontuação de 2 jogadores para 4 partidas. ao final exibero o total de pontos de cada jogador, seu nome, o vencedor e o total geral de pontos das partidas. Para isso você deverá utilizar uma matriz 2x4.
def maiornumero(numeros:int):
    maior = numeros[0]
    #pesquisa todo o vetor
    for n in numeros:
        #descobre quem é o maior
        if(n > maior):
            maior = n

#criando a matriz 2x4
#foi cirado uma coluna a mais para conter a soma de todos os pontos do jogador.
jogos = [[0 for partida in range(5)] for jogador in range(2)]
#cria um vertor de 2 elementos
jogadores = ['' for jogador in range(2)]

#entrada dos jogadores
for idx in range(2):
    jogadores[idx] = input(f'Digite o nome do {(idx + 1)}º Jogador: ')
    
#entrada das pontuações de cada jogo
for jogador in range(2):
    print("========================================")
    print(f"Jogador: {jogadores[jogador]}")
    for partida in range(4):
        jogos[jogador][partida] = int(input(f"Digite a pontuação da {partida + 1}º partida: "))
        
        #acumula o ponto desta partida na 5º coluna da matriz
        jogos[jogador][4] = jogos[jogador][4] + jogos[jogador][partida]
        
    if(jogador == 0):
        maior = jogos[jogador][4]
        ganhador = jogadores[jogador]
        
    if(jogos[jogador][4] > maior):
        maior = jogos[jogador][4]
        ganhador = jogadores[jogador]
        
print("==================== TOTAL DE PONTOS ====================")        
for jogador in range(2):
   
    print(f"jogador: {jogadores[jogador]} = {jogos[jogador][4]} ")
    
print(f"O vencedor é {ganhador}")