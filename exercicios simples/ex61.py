#fatorial de um numero

numero = int(input("fatorial de qual numero? : "))
fatorial = 1

for cont in range(numero, 0, -1): #vai do numero escolhido até 1
    
    if(cont > 1):
        print(f"{cont} x ", end='')
    else:
        print(f"{cont} = {fatorial}", end='')
    
    fatorial *= cont 

#print(f"O fatorial de {numero} é {fatorial}")