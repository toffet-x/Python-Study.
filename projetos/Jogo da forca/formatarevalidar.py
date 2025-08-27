# import os
# os.system('cls') or None
import unidecode
'''
  Função para printar os nomes dos alunos e partes que foram desenvolvidas do jogo por exemplo:
    - Aluno A
    - Aluno B
    - Aluno C
    - JOGO [ ]
    - DICAS [ ]
    - CONTROLE DE TEMPO [ ]
  
  *Criar o arquivo das palavras e dicas que vão ser utilizados (feito)(Apenas para desenvolvimento do jogo, pois o professor irá passar este arquivo)

  Criar função que ler o arquivo e formatar matriz com as palavras e dicas (feito)

  Começar sorteando uma palavra e exibindo a primeira dica na tela
    - A palavra deverá aparecer assim: _ _ _ _ _ _ _
    - E a dica assim: 'Dica: Essa é uma dica para aquela palavra'
  
  Criar função que valida a letra digitada pelo usuario:
    - Mostrar quais letras já foram digitadas (pode ser só as erradas mas seria legal mostrar todas)
    - Se a letra estiver correta formata a palavra adicionando a letra nela;
    - Se a letra estiver incorreta, salvar em uma lista de letras já escolhidas pelo usuario e remover uma vida mostrando uma parte do boneco
    - (dica usar while aqui) Validar se o usuraio digitou apenas um caracter e do tipo string, caso contrario avisar que ele digitou errado e solicitar novamente a letra

  Criar uma função para dar dica:
    - Caso o usuario digite 'DICA' deve se exibir a próxima dica. Neste caso o programa deverá se comportar como se o usuário tivesse errado uma letra (Ou seja remover uma vida/chance)
    - Se ele só puder errar mais uma letra e ele pedir uma dica, ele automaticamente perderá o jogo.

  Ao final do jogo, pergunte se o usuário deseja jogar novamente ou sair do jogo.

  Implementar o tempo máximo de jogo:
   - Caso o usuário demore mais do que este tempo, ele automaticamente perde o jogo.
'''

def le_formata_palavras(caminho):
  matriz_palavras_dicas = []
  # Abre o arquivo para leitura, com encoding = utf-8 ele formata corretamente os acentos e o 'ç'
  arq = open(caminho, "r", encoding='utf-8')
  conteudo = arq.readlines()
  
  # A variavel palavra_dica serve apenas de auxiliar para montar a matriz
  palavra_dica = []
  count = 0
  
  for linha in conteudo:
    # Valida se é palavra e adiciona na lista
    if(linha[0] == "P"):
      palavra_dica.append(linha[2:].strip())

    # Valida se é dica e adiciona na lista
    if(linha[0] == "D"):
      palavra_dica.append(linha[2:].strip())

    # valida se a palavra mudou para adicionar na matriz e zera minha lista
    if(count + 1 < len(conteudo) and linha[0] == "D" and conteudo[count+1][0] == "P"):
      matriz_palavras_dicas.append(palavra_dica)
      palavra_dica = []
    # Verifica se é o último conjunto de dicas da última palavra e adiciona na matriz
    if(count + 1 == len(conteudo)):
      matriz_palavras_dicas.append(palavra_dica)
      palavra_dica = []
    count += 1
  return matriz_palavras_dicas

matriz_palavra_dica = le_formata_palavras("jogo.txt")





def validacao(palavra):
  palavra_sem_acentos = unidecode.unidecode(palavra.lower()) #palavra sem acentos, usa unidecode e lower para não fazer diferença de caracteres maiusculos e com acentos
  palavra_original = palavra.lower()
  vidas = 5 #cabeça, torso, braço direito, braço esquerdo, perna direita, perna esquerda.
  letrasEscolhidas = []
  palavraFormatada = ['_' if letra.isalpha() else letra for letra in palavra_original] #basicamente formata a palavra baseado na original substituinda as letras por _ facilita na hora de exibir,

  while vidas > 0 and '_' in palavraFormatada: #loop continua enquanto as vidas forem maior que 0
      letra = "" #define a letra pra poder usar ela no loop
      while True: #segundo loop, enquanto a letra tiver tamanho diferente de 1 e não for alfabetetica o loop continua, break sai do loop
          letra = unidecode.unidecode(input("Digite uma letra: ").lower()) #mesmo processo dos acentos e lower, só que agora é input da letra.
          if (len(letra) == 1 and letra.isalpha()):
              break 
          print("Digite apenas um caractere.")

      if letra not in letrasEscolhidas: #se a letra não foi escolhida ela é adicionada e exibida
            letrasEscolhidas.append(letra)

            if letra in palavra_sem_acentos: #aqui verifica se a letra está na palavra
                print("Correto :D")
                for i in range(len(palavra_sem_acentos)): #é um loop que percorre i, e verifica se a letra existe na palavra.
                    if palavra_sem_acentos[i] == letra:
                        palavraFormatada[i] = palavra_original[i]
            else:
                print("Errado D:<")
                vidas = vidas - 1 #subtrai a vida...
      else: #esse else responde ao segundo if, se a letra já estiver já nas letras escolhidas ele vai pra cá.
            print("Você já escolheu essa letra.") 

      print("Letras escolhidas: ", end="") 
      for letra in letrasEscolhidas: #esse loop abre espaço na palavra
        print(letra, end=" ") #adiciona a letra e espaço
      print() #linha vazia / enter

      print("Palavra: ", end="") #mesma coisa que o de cima
      for letra in palavraFormatada:
        print(letra, end=" ")
      print() #linha vazia / enter

      print(f"Vidas restantes: {vidas}")

  if '_' not in palavraFormatada: #vê se existe algum _ na palavra, se não houver nenhum, quer dizer que o usuario ganhou...
        print("Venceste B)")
  else:
        print("Loserrr XD")

palavra = "computação" #tem que substituir essa parte com as palavras aleatorias e colocar as dicas...
validacao(palavra)




# def procuraDica(vetor, num):
#       if(vetor[num]== 'x') :
#     print(f"dica {num} repetida...")
#     return False
#   else:
#     vetor[num] = 'X'
#     return True