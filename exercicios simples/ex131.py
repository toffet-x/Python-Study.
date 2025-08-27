#crie uma função que receba um numero e seu expoente e exiba esse numero elevado ao expoente recebido.

def  func(base, exp):
   return base**exp
    
n1 = int(input("insira um valor: "))
n2 = int(input("insira o valor do expoente: "))

print(func(n1, n2))