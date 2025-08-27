import unidecode

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