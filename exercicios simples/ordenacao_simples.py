from random import randint
from random import shuffle

def gera(n, vmin, vmax):
    L = []
    for i in range(n):
        L.append(randint(vmin, vmax))
    return L


def crescente(L, n):
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            return False
        i += 1
    return True

def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def bogo_sort(L):
    n = len(L)
    while not crescente(L, n):
        shuffle(L)

def empurra(L, n):
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            troca(L, i, i+1)
        i += 1

def bubble_sort(L):
    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1



        
