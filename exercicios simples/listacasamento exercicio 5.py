###Você, um dos prováveis convidados para a cerimônia, decidiu dar como presente de casamento um programa
##que receberá como entrada os nomes dos convidados dos noivos e, no final, exibirá:
##
##
##
##  (a) A lista final de convidados;
##
##  (b) A lista com os que foram convidados apenas pela noiva;
##
##  (c) A lista com os que foram convidados apenas pelo noivo;
##
##  (d) A lista com os que foram convidados por ambos e;
##
##  (e) A lista com os que foram convidados por apenas um deles.
##
##
##
##Sabendo que os noivos elaboraram a lista de convidados separadamente, pode ocorrer de,
##ao combinarem as listas, inserirem nomes duplicados no programa.
##Por Mariana e Lucas estarem tão ocupados com outros preparativos,
##também é possível que, por distração, coloquem nomes duplicados na própria lista!
##Seu programa deve estar preparado para não duplicar os convites mesmo nessas situações.
##
##
##
##Note que os nomes dos convidados serão inseridos no programa de modo arbitrário, sem qualquer ordenação
##prévia e sempre associados a um dos noivos. Entretanto, para facilitar a vida do casal, seu programa deverá
##exibir os convidados de cada lista em ordem alfabética.
##
##
##
##Entrada
##A entrada será composta por zero ou mais linhas, em que cada linha é formada por um par de valores (X;Y)
##onde X representa o nome do convidado (somente letras minúsculas do alfabeto latino sem acentuação e espaços)
##e Y representa quem o convidou, podendo Y ser "noivo" ou "noiva" (sem aspas e em minúsculo).
##A entrada é finalizada com a leitura da palavra "ACABOU" (em maiúsculo e sem aspas).
##
##
##
##Saída
##A saída deverá corresponder ao que foi informado na descrição do problema e formatada conforme os
##casos de teste de exemplo. Tome cuidado com os títulos das listas apresentadas pelo programa e com
##os vinte hifens usados como borda para cada título. Também observe que ENTRE as listas existe um asterisco,
##mas não após a última.
##--------------------
##LISTA FINAL
##--------------------
##*
##--------------------
##APENAS NOIVA
##--------------------
##*
##--------------------
##APENAS NOIVO
##--------------------
##*
##--------------------
##POR AMBOS
##--------------------
##*
##--------------------
##POR APENAS UM DELES
##--------------------


def main():
    lnoivo = []
    lnoiva = []
    
    entrada = input()

    while entrada != 'ACABOU':

        nomeconv, noivx = entrada.split(';') #separa

        if noivx == 'noivo':
            if nomeconv in lnoivo: #não adiciona
                
            else:
                lnoivo.append(nomeconv) #adiciona
        elif noivx == 'noiva':
            if nomeconv in lnoiva:

            else:
                lnoiva.append(nomeconv)


    listafim = lnoivo[:] #copia rasa, não sei como fazer sem...
    
































































