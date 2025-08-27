# #exercicio48 48)	(STRING-VALIDACAO) Faça um programa que solicite do usuário nome, sexo e e-mail. Faça a seguinte validação nesses dados:
#a.	Nome : Deve ter pelo menos 3 caracteres
#b.	Sexo = M ou F ou I
#c.	e-Mail = deve possuir pelo menos o caractere @ e ter 10 letras no mínimo


nome = input("insira seu nome:")

while(len(nome) <= 3):
    print(f"Seu nome tem que ter mais de 3 caracteres")
    nome = input("insira seu nome:")

sexo = input("Sexo Biológico M ou F: ").upper()

while(sexo != 'M' and sexo != 'F'):
    sexo = input("Sexo Biológico: ").upper()
    
email = input(f"Insira um email valido: ")

while(len(email) < 10 or email.find('@') == -1):
    input(f"Insira um email valido: ")
        

