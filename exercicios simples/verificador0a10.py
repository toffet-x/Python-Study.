#programa que solicita do usuario um numero de 0 a 10, caso o contrario, erro

numero = int(input("numero: "))

while(numero > 10 or numero < 0):
    print(f"O numero tem que estar entre 0 e 10")
    numero = int(input("numero: "))
    
print(f"Ok")