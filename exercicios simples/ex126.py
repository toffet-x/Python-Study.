#Crie uma função que receba como parâmetro um caractere, verifique se este caractere contém uma das letras M, F, m, f, e escreva na tela a palavra 
def funcao(letra): 
    if(letra == 'f' or letra == 'F'):
        print("Femêa")
    elif(letra == 'm' or letra == 'M'):
        print("Macho")
    else:
        print("Invalido")    

coisa = input("insira m ou f: ")
funcao(coisa)