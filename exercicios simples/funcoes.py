from time import sleep

#fatorial
def fat(n):
    if n == 0:
        return 1
    elif n < 0:
        return n * fat(n+1)
    else:
        return n * fat(n-1)

#potencia
def pot(x,n):
    if n == 0:
        return 1
    else:
        return x * pot(x,n-1)

#soma de 1 até n
def temial(n):
    if n == 0:
        return 0
    else:
        return n + temial(n-1)

#contagem regressiva e progressiva
def cr(n):
    if n == 0:
        return
    else:
        print(n)
        sleep(1)
        cr(n-1)

#contagem progressiva
def cp(n):
    if n == 0:
        return
    else:
        cp(n-1)
        sleep(1)
        print(n)
