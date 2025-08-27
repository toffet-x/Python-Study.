#crie um programa que solicite do usuario 5 nomes de frutas, armazene-os em um vetor, e um unico caractere de pesquisa. crie uma rotina que busque dentro dos 5 nome de frutas quantas vezes esse caractere aparece em cada fruta. Exiba na tela as mensagens "Nome da fruta - 9999"

fruta = []

for f in range(5):
    fr = str(input("escreva uma fruta"))
    fruta.append(fr)

carater =  str(input("qual a letra: ")).lower

soma = 0

for loop in range (len(fruta)):
    for indice in range (len(fruta[loop])):
        if carater == indice:
            soma = soma + 1    
print("a letra {} se repete {} vezes na palavra {}".format(carater, soma, fruta))