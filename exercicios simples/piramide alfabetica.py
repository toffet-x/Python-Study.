def piramide(n, p):
    if n == 0:
        return
    else:
        piramide(n-1, p)
        print('.' * (26 - n), end='')
        if p == 'maiusculas':
            letra = 'A'
        else:
            letra = 'a'
        for i in range(n):
            print(letra, end='')
            letra = chr(ord(letra) + 1)
        print()

def main():
    n, p = input().split()
    n = int(n)
    piramide(n, p)

main()
