from pylab import plot, show, legend, title, xlabel, ylabel, grid

def arq_para_graf(caminho):
    #Lista para armazenar as legendas
    leg = []

    #Abre e lê o arquivo de dados
    with open(caminho) as arq:
        for linha in arq:
            #Lê a expressão e os valores mínimo e máximo para o eixo-x
            expr, xmin, xmax = linha.split()
            xmin, xmax = int(xmin), int(xmax)
            
            #Gera o intervalo de x para o gráfico
            xs = range(xmin, xmax + 1)
            
            #Converte a expressão em uma função
            funcao = eval('lambda x: ' + expr)
            ys = [funcao(x) for x in xs]  #Calcula os valores de y
            
            #Plota a expressão com o intervalo de x fornecido
            plot(xs, ys, label=expr)  #Usa a expressão como legenda
            leg.append(expr)  #Adiciona a expressão à lista de legendas

    
    legend()  #Exibe as legendas
    show()


caminho = input("Arquivo de dados (.txt): ")



arq_para_graf(caminho)

