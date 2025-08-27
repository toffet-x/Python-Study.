n1 = input(f"Primeiro numero: ")

while(not n1.isdecimal()):
    n1 = input(f"Primeiro numero: ")

n2 = input(f"Segundo numero de {len(n1)} digitos: ")

while(len(n2) != len(n1) or not n2.isdecimal()):
    n2 = input(f"Segundo numero de {len(n1)} digitos: ")


resultado = 0
for conta in range(len(n1)):
    resultado += int(n1[conta])*int(n2[conta])

for resolução in range(len(n1)):

    if resolução < len(n1) - 1:
        print(f"{n1[resolução]} x {n2[resolução]} +", end = ' ')
    else:
        print(f"{n1[resolução]} x {n2[resolução]} :", end = ' ')

print(f"resultado da soma = {resultado}")

