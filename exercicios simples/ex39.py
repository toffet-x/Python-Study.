#39)	(STRING) Solicitar do usuário dois números de 3 posições cada. Apresentar o valor da multiplicação de cada posição de um numero pelo outro. EX
#123
#456
#1*4 + 2*5 + 3*6



n1 = input(f"Primeiro numero de 3 digitos: ")

while(len(n1) != 3 or not n1.isdigit()):
    n1 = input(f"Primeiro numero de 3 digitos: ")

n2 = input(f"Segundo numero de 3 digitos")

while(len(n2) != 3 or not n2.isdigit()):
    n2 = input(f"Segundo numero de 3 digitos")

resultado = int(n1[0])*int(n2[0]) + int(n1[1])*int(n2[1]) + int(n1[2])*int(n2[2])
print(f"{n1[0]} x {n2[0]} + {n1[1]} x {n2[1]} + {n1[2]} x {n2[2]} = {resultado}") 