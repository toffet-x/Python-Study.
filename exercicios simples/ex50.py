#50)	(LAÇO) Crie um programa que calcule e escreva a quantidade de grãos de milho que se pode colocar num tabuleiro de xadrez, conforme regra definida abaixo:
#a.	Um tabuleiro de xadrez possui 64 casas, na primeira casa se coloca 1 grão, nas casas subsequentes será colocado o dobro de grãos da casa anterior.

qtdtotal = 1
graoscasa = 1

#laco
for casa in range (2, 65, 1): #começa da casa 2, pois a casa 1 ja tem 1 grao
    
    graoscasa *= 2 #multiplica a casa anterior por 2
    qtdtotal += graoscasa #acumula a quantidade de graos
    
print(f"quantidade total de grãos: {qtdtotal}")