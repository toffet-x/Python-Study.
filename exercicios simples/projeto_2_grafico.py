from pylab import plot, show, grid, legend, xlabel, ylabel, title

def plota(expressao, xs, g, legenda):  # xs = domínio
    #Define a função usando eval com uma expressão lambda
    funcao = eval('lambda x: ' + expressao)
    
    #Calcula os valores de y para cada valor em xs
    ys = [funcao(x) for x in xs]
    
    #Configuração do gráfico
                                 
    plot(xs, ys, label=legenda)  #Usa o rótulo fornecido como legenda.
    
    legend()
    grid(g)  #Exibe o grid
    show()

#Entrada de dados
expressao = input("Expressão: ")
xs = input("Valores de x: ").split()
xs = [float(x) for x in xs]
grade = input("Exibir grid? [s/n]: ")
grade = True if grade.lower() == 's' else False

 

legenda = input("Legenda: ")

#Chama a função para plotar
plota(expressao, xs, grade, legenda)


