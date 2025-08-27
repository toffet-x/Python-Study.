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
    lnoivo = set()
    lnoiva = set()
 
    
    entrada = input()

    while entrada != 'ACABOU':
        
        nomeconv, noivx = entrada.split(';') #separa
        #L = lista
        if noivx == 'noivo':
            lnoivo.add(nomeconv)
        else:
            lnoiva.add(nomeconv)

        entrada = input()

        #ap = apenas
        # lista final união
    listafim = lnoivo | lnoiva
    listafim = sorted(listafim)
        # lista convidados noiva
    apnoiva = lnoiva - lnoivo
    apnoiva = sorted(apnoiva)
        # lista convidados noivo
    apnoivo = lnoivo - lnoiva
    apnoivo = sorted(apnoivo)
        # lista noivo e noiva
    lista2 = lnoivo & lnoiva
    lista2 = sorted(lista2)
        # por apenas 1
    ap1 = lnoivo ^ lnoiva
    ap1 = sorted(ap1)

        #formatação
    #todos
    print('-'*20)
    print('LISTA FINAL')
    print('-'*20)
    for convidado in listafim:
        print(convidado)
    print('*')

    #apenas novia

    print('-'*20)
    print('APENAS NOIVA')
    print('-'*20)
    for convidado in apnoiva:
        print(convidado)
    print('*')

    #apenas noivo

    print('-'*20)
    print('APENAS NOIVO')
    print('-'*20)
    for convidado in apnoivo:
        print(convidado)
    print('*')
        
    #ambos

    print('-'*20)
    print('POR AMBOS')
    print('-'*20)
    for convidado in lista2:
        print(convidado)
    print('*')

    #por apenas um deles

    print('-'*20)
    print('POR APENAS UM DELES')
    print('-'*20)
    for convidado in ap1:
        print(convidado)
    

        
main()           
    
































































