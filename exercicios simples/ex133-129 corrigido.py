#exercicio 129 Crie uma função que calcule se um determinado número é primo, devolva para isso verdadeiro ou falso. No programa principal, solicite do usuário um número e verifique se o mesmo é primo ou não usando a função criada.

def primo(numero:int) :
    
    if(numero <= 1):
        return False
    
    
    #vai do 2 ao (numero - 1)
    for i in range(2, numero):
        if(numero % i == 0):
            return False
    
    
    return True

num = int(input("Digite um número: "))

if(primo(num)):
    print("Este numero é primo!!!")
else:
    print("Este número não é primo!!!")
    
    
    
