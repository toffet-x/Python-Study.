import os # Biblioteca para limpar o console
import random # Biblioteca para para sortear um número
 # Biblioteca para mudar o estilo da fonte do console
import time # Biblioteca para controlar o tempo (tipo uma joia do infinito)

#made by Christopher de Moura Oliveira, Thiago Alves de Oliveira, João Vitor Bastida  


indice_palavras_sorteadas = []

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

def sorteia_um_da_lista(palavras_para_sortear, indices_sorteados, e_dica):
  minimo = 0
  if e_dica:
    minimo = 1

  # Sorteia um número inteiro de 0 até a quantidade de palavras encontradas
  num = random.randint(minimo, len(palavras_para_sortear)-1)

  # Valida se o número sorteado ja foi escolhido, caso verdadeiro sortera outro número
  while(num in indices_sorteados):
    num = random.randint(minimo, len(palavras_para_sortear)-1)

  return palavras_para_sortear[num], num

def printa_nomes():
  # Muda a cor da fonte

  print("Christopher de Moura Oliveira")
  print("Thiago Alves de Oliveira")
  print("João Vitor Bastida \n")
  print("Jogo [x]")
  print("Dicas [x]")
  print("Controle de Tempo [x] \n")
  print("Bem vindo(a) ao nosso jogo da forca. Você terá 6 vidas para acertar a palavra. Boa sorte! \n")
  
def formata_palavra(palavra, letras_corretas):
  palavra_formatada = ""
  for x in palavra:
    if (unicode_improvisado(x).lower() in unicode_improvisado(letras_corretas)):
      palavra_formatada += f"{x} "
    elif (x == " "):
      palavra_formatada += "  "
    else:  
      palavra_formatada += "_ "
  return palavra_formatada

def print_boneco(vidas_restante):
  boneco = [" O\n", "/", "|", "\\\n", "/", " \\"]


  if vidas_restante > len(boneco) or vidas_restante < 0:
    return "Número de vidas invalido"
  total_de_vidas = 6
  qtd_vidas_perdidas = total_de_vidas - vidas_restante
  print("------------------------------------")
  print(f"Você tem {vidas_restante} vidas restante")
  for x in range(qtd_vidas_perdidas):
    print(boneco[x], end="")
  print("\n------------------------------------")


def valida_input_usuario(input_usuario, letras_digitadas):
  # Verifica se o input do usuario é do tipo alpha, se foi digitado apenas um caracter e se a letra não é repetida
  if (not input_usuario.isalpha() or len(input_usuario) != 1 or input_usuario.lower() in letras_digitadas):
    # Retorna falso caso NÃO seja um input valido
    return False
  else:
    # Retorna vaerdadeiro caso seja um input valido
    return True

def finaliza_rodada(msg_para_usuario):
  vai_jogar_novamente = input(f"{msg_para_usuario} Deseja jogar novamente ? [s/n]: ")
  
  # Valida se o usuario digitou "s" ou "n"
  while vai_jogar_novamente.lower() != "s" and vai_jogar_novamente.lower() != "n":
    vai_jogar_novamente = input("Input invalido. Deseja jogar novamente ? digite 's' para SIM e 'n' para NÃO: ")
  
  # Chama a função do inicio do jogo caso o usúario tenha digitado "s"
  if vai_jogar_novamente == "s":
    print("Reiniciando...")
    inicia_jogo()
  
  # Finaliza e sai do jogo caso o usúario tenha digitado "n"
  else:
    print("Volte Sempre!")

def reinicia_o_jogo():
  print("Parabéns se você chegou até aqui é porque usou todas as palavras e por algum motivo milagroso /\ o jogo não bugou.")
  vai_reiniciar_o_jogo = input(f"Deseja jogar novamente do zero? [s/n]: ")
  
  # Valida se o usuario digitou "s" ou "n"
  while vai_reiniciar_o_jogo.lower() != "s" and vai_reiniciar_o_jogo.lower() != "n":
    vai_reiniciar_o_jogo = input("Nessa altura do jogo você ainda digita errado? Fala sério né. Tenta outra vez vai, vamos lá você consegue: ")
  
  # Chama a função do inicio do jogo caso o usúario tenha digitado "s"
  if vai_reiniciar_o_jogo == "s":
    # Reseta a variavel com o indice das palavras sorteadas
    for index in range(len(indice_palavras_sorteadas)-1):
      del(indice_palavras_sorteadas[index])
    print("Reiniciando...")
    inicia_jogo()
  
  # Finaliza e sai do jogo caso o usúario tenha digitado "n"
  else:
    print("Volte Sempre!")

def unicode_improvisado(palavra):
  palavra_formatada = list(palavra)
  letras_especiais = [
      ["a", "à", "á", "ã", "â"],
      ["e", "è", "é", "ê"],
      ["i", "ì", "í", "î"],
      ["o", "ò", "ó", "õ", "ô"],
      ["u", "ù", "ú", "û"],
      ["c", "ç"]
    ]

  # Percorre a palavra e substitui os acentos por letras sem acentos além do "ç" pelo "c"
  for index_letra in range(len(palavra)):
      for letras in letras_especiais:
          if palavra_formatada[index_letra].lower() in letras:
              if palavra_formatada[index_letra].islower():
                palavra_formatada[index_letra] = letras[0]
              else:
                palavra_formatada[index_letra] = letras[0].upper()
                  
  # Junta a palavra e retorna ela formatada
  return "".join(palavra_formatada)

def acertou_a_letra(palavra, letra):
  palavra_sem_acentos = unicode_improvisado(palavra)
  
  # Valida se a letra digitada está na palavra
  if (letra.lower() not in palavra_sem_acentos.lower()):
    return False
  else: 
    return True  

def printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, msg_tempo):
  print(msg_tempo)
  print(f"Letras escolhidas: {letras_escolhidas}")
  print_boneco(vidas_restante)
  print(palavra_formatada)
  print("DICA: ", end="(")
  for dica in indice_dicas_sorteadas:
    print(f"{palavra_sorteada[dica]}", end=", ")
  print(")")

def inicia_jogo():
  letras_escolhidas = []
  indice_dicas_sorteadas = []
  palavras_com_dicas = le_formata_palavras("jogo.txt")

  if (len(palavras_com_dicas) == len(indice_palavras_sorteadas)):
    return reinicia_o_jogo()

  palavra_sorteada, novo_indice_palavra = sorteia_um_da_lista(palavras_com_dicas, indice_palavras_sorteadas, False)
  indice_palavras_sorteadas.append(novo_indice_palavra)

  dica_sorteada, novo_indice_dica = sorteia_um_da_lista(palavra_sorteada, indice_dicas_sorteadas, True) # Esse [1:] serve para pular a palavra e pegar apenas as dicas
  indice_dicas_sorteadas.append(novo_indice_dica)
  vidas_restante = 6
  palavra_formatada = formata_palavra(palavra_sorteada[0], letras_escolhidas)

  printa_nomes()


  printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, "")
  while palavra_formatada.find("_") != -1:
    msg_status_tempo = "Você está dentro do limite de tempo continue assim ;) "
    if (vidas_restante == 0):
      return finaliza_rodada(f"Que pena, Você perdeu o jogo.\n A palavra era: {palavra_sorteada[0]}.\n")
    
    # Formata o input do usuario caso ele tenha digitado a letra com acento
    inicial = time.time()
    print("Você tem 10 segundos para digitar uma letra, se passar desse tempo você perdera uma vida.")
    input_usuario = unicode_improvisado(input("Digite uma letra: ")).lower()
    final = time.time()

    if (final - inicial > 5):
      vidas_restante -= 1
      msg_status_tempo = "Demourou d+ perdeu uma vida :( "
      printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, msg_status_tempo)

    # Função para limpar o terminal
    os.system('cls') 
    if (input_usuario.lower() == unicode_improvisado(palavra_sorteada[0].lower())):
      return finaliza_rodada(f"Parabéns você ganhou.\n")
    
    if (input_usuario.lower() == "dica"):
      if vidas_restante == 1:
        finaliza_rodada()
      else:
        if (len(palavra_sorteada[1:]) == len(indice_dicas_sorteadas)):
          print("Dicas esgotadas!!!")
          printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, msg_status_tempo)
        else:
          dica_sorteada, novo_indice_dica = sorteia_um_da_lista(palavra_sorteada, indice_dicas_sorteadas, True) # Esse [1:] serve para pular a palavra e pegar apenas as dicas
          indice_dicas_sorteadas.append(novo_indice_dica)
          vidas_restante -= 1
          palavra_formatada = formata_palavra(palavra_sorteada[0], letras_escolhidas)
          printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, msg_status_tempo)
    else:
      a_letra_foi_valida = valida_input_usuario(input_usuario, letras_escolhidas)
      while (not a_letra_foi_valida):
        input_usuario = input("Letra invalida ou repetida. Digite novamente: ")
        a_letra_foi_valida = valida_input_usuario(input_usuario, letras_escolhidas)
      
      letras_escolhidas.append(input_usuario)
      palavra_formatada = formata_palavra(palavra_sorteada[0], letras_escolhidas)
 
      if (not acertou_a_letra(palavra_sorteada[0], input_usuario)):
        vidas_restante -= 1
      printa_estado_do_jogo(palavra_formatada, vidas_restante, palavra_sorteada, letras_escolhidas, indice_dicas_sorteadas, msg_status_tempo)
  return finaliza_rodada(f"Parabéns você ganhou.\n")

inicia_jogo()
