#exercicio 102
#crie um programa que solicite do usuario 10 nome e 10 salarios armazena cada um deles em um vetor. ao final apresente os nomes dos funcionarios que recebem mais do que a media geral entre os 10 funcionairos cadastrados

#forma a string vazia > repete 10 vezes ''
nome = ["" for bingus in range(10)]
#cria uma string com 10 0.0
salario = [0.0 for sal in range(10)]

media = 0.0
soma = 0

#entrada de dados
for indice in range(len(nome)):
    nome[indice] = (input("Digite seu nome: "))
    
    salario[indice] = int(input("Digite seu salario: "))
    soma += salario[indice]

media = soma / len(salario)

for dado in range(len(salario)):
    if salario[dado] > media:
        print(f"{nome[dado]} Recebe mais: {salario[dado]}", end=" | ")
print(f"\na media é {media}")