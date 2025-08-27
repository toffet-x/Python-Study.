#Faça um programa que solicite do usuário 10 números, esses números devem estar entre 1 e 100, caso esteja fora desse intervalo não aceite o número. Ao final exiba quantos números são maiores que 20 e quantos números são menores que 10.
#criação de variaveis fora do laço
maior20 = menor10 = 0

#laço para 10 numeros
for contador in range(10):
    
    #entrada
    numero = int(input(f"digite o {contador + 1}° numeros: "))
    
    #validação
    while(numero > 100 or numero < 0):
        print("numero invalido")
        numero = int(input(f"digite o {contador + 1}° numeros: "))

    
    #contadores de numeros menores que 10 e maiores que 20
    #dentro do laço pra poder contar
    if(numero > 20):
        maior20 += 1
    elif(numero < 10):
        menor10 += 1
    
#print fora do laço pra não ficar repetindo    
print(f"maiores que 20 = {maior20}")
print(f"menores que 10 = {menor10}")