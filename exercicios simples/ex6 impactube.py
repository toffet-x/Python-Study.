def main():
    qtd = int(input())
    tabela = []
    
    for x in range(qtd):
        desempacotar = input()
        canal, inscritos, money, bonus = desempacotar.split(';')

        inscritos = int(inscritos)
        money = float(money)
        if bonus == 'sim':
            bonus = True
        else:
            bonus = False

        tabela.append([canal, inscritos, money, bonus])

    X = float(input())
    Y = float(input())

    
    print('-'*5)
    print('BÔNUS')
    print('-'*5)

    for canal, inscritos, money, bonus in tabela:
        if bonus:
            boni = (inscritos // 1000) * X
        else:
            boni = (inscritos // 1000) * Y


        print(f'{canal}: R$ {boni + money:.2f}')
        

main()
