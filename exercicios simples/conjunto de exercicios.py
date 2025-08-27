def exer_22():
    '''
    22)	(IF/OPERADOR LÓGICO) Faça um programa que informe em qual faixa de valores o a informação se encaixa:
        De 0 a 10 (faixa 1)
        De 15 a 25 (faixa 2)
        De 26 a 40 (faixa 3)
    Qualquer coisa que não se enquadre nestas faixas informe que o valor não possui faixa definida
    '''
    valor = float(input("Digite um número: "))

    if valor >= 0 and valor <= 10:
        print("Faixa 1")
    elif valor >= 15 and valor <= 25:
        print("Faixa 2")
    elif valor > 25 and valor <= 40:
        print("Faixa 3")
    else: 
        print("Esse valor não possui faixa definida.")

def exer_23():
    '''
    23)	(IF/OPERADOR LÓGICO) Solicitar do usuário uma determinada idade de um nadador. Baseado nesta idade indique qual a categoria ao qual ele pertente:
        •	Sem Categoria  menor que 5 anos;
        •	Infantil A 5 – 7 anos;
        •	Infantil B 8 – 10 anos;
        •	Juvenil A 11 – 13 anos;
        •	Juvenil B 14 – 17 anos;
        •	Adulto 18 – 60 anos;
        •	Senior Acima de 60 anos
    '''
    idade = int(input("Digite sua idade: "))

    if idade < 5:
        print("Sem categoria menor")
    elif idade < 8:
        print("Infantil A")
    elif idade < 11:
        print("Infantil B")
    elif idade < 14:
            print("Juvenil A")
    elif idade < 18:
        print("Juvenil B")
    elif idade < 61:
        print("Adulto")        
    elif idade > 60: 
        print("Sênior acima de 60 anos")

def exer_23_b():
        
    idade = int(input("Digite sua idade: "))

    if idade < 5:
        print("Sem categoria menor")
        
    if idade >= 5 and idade < 8:
        print("Infantil A")
        
    if idade >= 8 and idade < 11:
        print("Infantil B")
        
    if idade >= 11 and idade < 14:
        print("Juvenil A")
            
    if idade >= 14 and idade < 18:
        print("Juvenil B")
        
    if idade >= 18 and idade < 61:
        print("Adulto")  
              
    if idade > 60: 
        print("Sênior acima de 60 anos")

def exer_25():
    '''
    (IF) Solicitar do usuário 4 notas. Calcular a média aritmética. Informar se o aluno está aprovado ou não, seguindo os critérios:
        Media >=7 - Aprovado
        Media < 7 - Fazer prova de Exame, solicitar essa nota de exame
        Calcular nova média, média antiga + exame dividido por 2
        novaMedia >=6 - Aprovado Exame
        novaMedia <6 - Reprovado

    '''
    p1 = float(input("Nota da P1: "))
    p2 = float(input("Nota da P2: "))
    p3 = float(input("Nota da P3: "))
    p4 = float(input("Nota da P4: "))

    media = (p1+p2+p3+p4) / 4
    
    if media >= 7:
        print("Aprovado :) !")
    else:
        print("Ficou de recuperação.")
        exame = float(input("Digite a nota do exame: "))
        nova_media = (exame + media) / 2
        if nova_media >= 6:
            print("Aprovado Exame!")
        else:
            print("Reprovado :(")

def exer_50():
    qtdTotal = 1
    graosCasa = 1
    for casa in range(2, 65, 1):
        graosCasa *= 2
        qtdTotal += graosCasa
    print(qtdTotal)

def exer_53():
    resultado = 0
    numero = int(input("Qual a tabuada: "))
    for cont in range(10,0,-1):
        resultado = numero * cont
        print(f"{numero} X {cont} = {resultado}")

def exer_54():
    soma = 0
    for numero in range(1, 101, 1):
        soma += numero
    print(f"A somatória é: {soma}")

def exer_56():
    '''
    56)	(LAÇO) Solicite do usuário 4 notas, faça a validação para aceitar valores entre 0 e 10,
    apresente no final a média ponderada das notas, sendo os pesos 2, 3, 5, 6 respectivamente.
    '''
    nota_1 = float(input("Digite a 1ª nota: "))
    while(nota_1 < 0 or nota_1 > 10):
        nota_1 = float(input("Nota invalida. Digite novamente a 1ª nota: "))

    nota_2 = float(input("Digite a 2ª nota: "))
    while(nota_2 < 0 or nota_2 > 10):
        nota_2 = float(input("Nota invalida. Digite novamente a 2ª nota: "))

    nota_3 = float(input("Digite a 3ª nota: "))
    while(nota_3 < 0 or nota_3 > 10):
        nota_3 = float(input("Nota invalida. Digite novamente a 3ª nota: "))

    nota_4 = float(input("Digite a 4ª nota: "))
    while(nota_4 < 0 or nota_4 > 10):
        nota_4 = float(input("Nota invalida. Digite novamente a 4ª nota: "))

    media = ((nota_1*2) + (nota_2*3) + (nota_3*5) + (nota_4*6))/(2+3+5+6)
    print(f"A média ponderada das notas é {media}")

def exer_60():
    '''
    60)	(LAÇO) Crie um programa que solicite do usuário quantos produtos ele quer cadastrar (utilize o FOR/PARA), dentro desse laço, solicite o tipo de um produto qualquer, onde esse tipo só pode ser “F” ou “S” (Físico, Serviço) (fazer validação com DO WHILE/REPITA), e o preço do produto com 3 casas decimais. Apresente ao final do laço quantos produtos são físicos e quantos são Serviço e apresente o preço médio de cada tipo, com 3 casas decimais e que ocupe 10 espaços.
    '''
    qtd_fisico = 0
    qtd_servico = 0
    valor_fisico = 0
    valor_servico = 0

    qtd_pdr = int(input("Digite quantos produtos deseja cadastrar? "))
    for cont in range(qtd_pdr):
        pdr_tipo = input("Digite 'F' para produtos fisicos ou 'S' para serviços? ")
        while(pdr_tipo != "F" and pdr_tipo != "S"):
            print("Caracter invalido, certifique-se de usar letras maiusculas e tente novamente!")
            pdr_tipo = input("Digite 'F' para produtos fisicos ou 'S' para serviços? ")
        
        if(pdr_tipo == "F"):
            qtd_fisico += 1
            value = float(input("Qual o valor desse produto? "))
            valor_fisico += value
        
        if(pdr_tipo == "S"):
            qtd_servico += 1
            value = float(input("Qual o valor desse produto? "))
            valor_servico += value
    
    print(f"Ao todo são {qtd_fisico} produtos fisicos com uma média de {(valor_fisico / qtd_fisico):.3f} e {qtd_servico} serviços com uma méida de {(valor_servico / qtd_servico):.3f}")

def exer_fatorial():
    numero = int(input("Fatorial de qual número: "))
    fatorial = 1
    print(f"{numero}! = ", end="")
    for cont in range(numero, 0, -1):
        fatorial *= cont
        
        # print(f"O fatorial de {numero} é {fatorial}")
        if(cont > 1):
            print(f"{cont} x ", end="")
        else:
            print(f"{cont} = {fatorial} ", end="")

def exer_63():
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))

    qtd_menor_1 = 0
    qtd_maior_2 = 0

    for cont in range(10):
        new_num = int(input(f"Digite o {cont+1}º número: "))
        if (new_num < num_1):
            qtd_menor_1 += 1

        if (new_num > num_2):
            qtd_maior_2 += 1
    print(f"Você digitou {qtd_menor_1} números menores que {num_1} e {qtd_maior_2} números maiores que {num_2}.")

def exer_39():
    n1 = input("Digite um número com 3 posições:")
    while(len(n1) != 3 or not n1.isdigit()):
        n1 = input("Valor invalido! Digite apenas 3 números: ")

    n2 = input("Digite um número com 3 posições:")
    while(len(n1) != 3 or not n1.isdigit()):
        n2 = input("Valor invalido! Digite apenas 3 números: ")

    soma = 0
    for position in range(3):
        soma += int(n1[position]) * int(n2[position])

    print(f"A soma é: {soma}")

def exer_43():

    # (STRING) Crie um programa em C que solicite do usuário um texto com no máximo 60 caracteres. Solicite também quantas letras ele quer mostrar do texto e a partir de qual posição. Faça a apresentação desse trecho solicitado na ordem direta e na ordem indireta.

    x = "faculdade"

    qtd = 4
    partir = 2
    # print(partir+qtd)
    print(x[2:6])

def exer_44():
    frase = input('Digite uma frase com duas palavras: ')
    while(frase.find(' ') == -1 or frase[0] == ' ' or frase[len(frase) - 1]):
        frase = input("Não possui 2 palavras! Digite uma frase com duas palavras: ")

    espaco = frase.find(' ')
    # novaFrase = frase[espaco+1:]
    # novaFrase += novaFrase + ' ' + frase[0:espaco]

    novaFrase = f"{frase[espaco+1:]} {frase[0:espaco]}"
    print(novaFrase)

