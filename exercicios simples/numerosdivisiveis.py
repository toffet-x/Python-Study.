#quantos numeros de 0 a 1000 são divisivei por 2 4 7
divisiveis2 = divisiveis4 = divisiveis7 = 0

for contador in range(1001):
    
    #para saber quais são os numeros divisiveis colocar print(divisivei_por_{n}) na if do valor
    
    if(contador % 2 == 0):
        divisiveis2 += 1
        
    if(contador % 4 == 0):
        divisiveis4 += 1
        
    if(contador % 7 == 0):
        divisiveis7 += 1
        
        
print(divisiveis2)
print(divisiveis4)
print(divisiveis7)