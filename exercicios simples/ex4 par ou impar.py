def parimpar(numero):
    
    if numero > 1:
        return parimpar(numero -2)
    if numero == 1:
        return False
    else:
        return True


if parimpar(int(input())):
    print('numero par')
else:
    print('numero nao par')
