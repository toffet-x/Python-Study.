#119)	(Matriz) Crie um programa em C que solicite do usuário o preenchimento de uma matriz 6X6, após a entrada informe o valor da soma da diagonal principal e da soma da diagonal secundária

import random #biblioteca para numeros randomicos
tamanho = int(input("Qual o tamanho da matriz? "))
matriz = [[0 for col in range(tamanho)] for lin in range(tamanho)]

#entrada de dados
for lin in range(len(matriz)): #obtem quantas linhas
    for col in range(len(matriz[lin])): #obtem quantas colunas desta linha
        #matriz[lin][col] = int(input(f"Digite [{lin}][{col}]:"))
        #Gera numeros randomicos entre 1 e 100 inclusive
        matriz[lin][col] = random.randint(1, 100)
        print(f"Digite [{lin}][{col}]: {matriz[lin][col]}")
        
#Diagonal principal
soma = 0
for idx in range(len(matriz)) :
    soma = soma + matriz[idx][idx]

print(f"Diagonal Principal = {soma}")    

#Diagonal secundária
maximo = len(matriz) - 1
soma = 0
for idx in range(len(matriz)) :
    soma = soma + matriz[idx][maximo - idx]
    
print(f"Diagonal Secundária = {soma}")    