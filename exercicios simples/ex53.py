#Resolva o exercício anterior mostrando a tabuada de trás para frente.
resultado = 0
numero = int(input("qual a tabuada: "))

for cont in range(10, 0, -1):
    resultado = numero * cont
    print(f"{numero} x {cont} = {resultado}", end=' | ')