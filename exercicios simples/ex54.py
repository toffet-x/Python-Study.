#Utilizando o laço de repetição, apresente a soma dos números existentes entre 1 e 100 inclusive. (1+2+3+4+5+6….+99+100). Efetuar o teste de mesa dos 4 primeiros elementos


soma = 0
for numero in range(1, 101, 1):
    soma += numero

print (f"A somatoria é: {soma}")

