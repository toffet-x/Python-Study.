from pylab import plot, show, axis, grid, title, xlabel, ylabel, legend

#função para o projeto do onibus só. Não sabia se era pra fazer os 3 do projeto 1
def arq_para_graf(caminho, titulo, label_x, label_y, grade):
    xs = []
    ys1 = []
    ys2 = []
    leg = []
    #Lê o arquivo de dados OBS: tem que colocar o nome completo e extensão
    #ex: onibus_metro.txt
    #obs2: o arquivo tem que estar na mesma pasta que o codigo...
    with open(caminho) as arq:
        #Lê as duas primeiras linhas como legendas
        leg.append(arq.readline().strip())
        leg.append(arq.readline().strip())
        
        #Lê o restante das linhas e extrai os dados
        for s in arq:
            x, y1, y2 = s.split()
            xs.append(int(x))
            ys1.append(float(y1))
            ys2.append(float(y2))
    
    #Configurações do gráfico
    title(titulo)
    xlabel(label_x)
    ylabel(label_y)
    grid(grade)
    plot(xs, ys1, label=leg[0])  #Gráfico para ys1 com legenda, cria a legenda definida em leg[0]
    plot(xs, ys2, label=leg[1])  #Gráfico para ys2 com legenda, igual o de cima só que leg[1]
    legend()  #Exibe a legenda, sem argumento ele usa o valor do label.
    show()

#Recebe o caminho do arquivo e variáveis para o gráfico
caminho = input("Arquivo de dados (.txt): ")
titulo = input("Título: ")
label_x = input("Rótulo do eixo x: ")
label_y = input("Rótulo do eixo y: ")
grade = input("Grade? [s/n]: ")
grade = True if grade == 's' else False

#Chama a função
arq_para_graf(caminho, titulo, label_x, label_y, grade)

