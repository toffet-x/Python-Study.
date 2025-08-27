#44)	(STRING) Crie um programa em portugol que solicite do usuário um texto com 2 palavras. Faça essa validação verificando se existe 1 espaço em branco, em seguida troque o conteúdo entre as duas e as apresente

frase = input("digite uma frase com duas palavras: ")
while(frase.find(' ') == -1 and (frase[0] == ' ' or frase[len(frase) - 1] == ' ')):
    print("Frase não possui duas palavras...")
    frase = input("Digite uma frase com udas palvras: ")

espaço = frase.find(' ') #encontra o espaço
novaFrase = frase[espaço + 1:] #pega do espaço até o final > 1:?
novaFrase += ' ' + frase[0:espaço] #pega do inicio até o espaço

print(f"trocado: {novaFrase}")
