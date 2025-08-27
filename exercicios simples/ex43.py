# 43)	(STRING) Crie um programa em C que solicite 
# do usuário um texto com no máximo 60 caracteres. 
# Solicite também quantas letras ele quer mostrar 
# do texto e a partir de qual posição. Faça a 
# apresentação desse trecho solicitado na ordem 
# direta e na ordem indireta.

frase = input("Digite uma frase com no máximo 60 caracteres:")
while (len(frase) > 60):
    frase = input("Erro, digite uma frase com no máximo 60 caracteres:")

qtd = int(input("Quantas letras que buscar? "))    
partir = int(input("A partir de qual posição? "))

print("Direto: ", end='')
for posicao in range(qtd):
    print(frase[partir + posicao], end='')

#outra forma de fazer direto
print(f"\nDireto: {frase[partir:partir+qtd]}")    
    
print("\nInverso: ", end='')
for posicao in range(qtd-1, -1, -1):
    print(frase[partir + posicao], end='') 