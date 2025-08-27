# solicitar do usuario 10 numeros, apresentar quais são maiores que zero juntamente de sua somatoria

qtd = soma = 0

for vez in range(10): # 10 vezes
    numero = int(input(f"Digite o seu {vez+1}º numero :"))
    
    #testa
    if(numero >= 0):
        qtd += 1 #qtd = qtd + 1
        soma += numero # soma = soma + numero
        
print(f"o total de numeros maiores que zero é: {qtd}")
print(f"a somatoria desses numeros é: {soma}")
