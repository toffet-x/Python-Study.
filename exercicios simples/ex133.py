#crie uma função que verifique se um determinado numero é primo
#essa função deve receber como parametro um numero e verificar dentro dele se este numero é
#primo ou não, e devolver um valor booleano (true/false).
#faça o programa principal que solicite esse numero para o usuario e chame a função.

def verp(valor):
    if(valor == 2 or valor == 3 or valor == 5 or valor == 7):
        return "primo"
    elif(valor % 2 == 0 or valor % 3 == 0 or valor % 5 == 0 or valor % 7 == 0):
        return "não primo"
    else:
        return "primo"
    
numero = int(input("insira um numero: "))

x = verp(numero)

print(x)
