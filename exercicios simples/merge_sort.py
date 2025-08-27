from ordenacao_simples import *
from time import time

def tempo(f, *a):
    inicio = time()
    f(*a)
    return time() - inicio

def intercala3(L, inicio, meio, fim):
    T = (fim - inicio + 1) * [0]
    i, j, k = inicio, meio+1, 0

    while i <= meio and j <= fim:
        if L[i] < L[j]:
            T[k] = L[i]
            i += 1
    
        else:
            T[k] = L[j]
            j += 1
        k += 1

    while i <= meio:
        T[k] = L[i]
        i += 1
        k += 1

    while j <= fim:
        T[k] = L[j]
        j += 1
        k += 1

    for i in range(0, len(T)):
        L[inicio+i]  = T[i]

def merge_sort(L, inicio, meio, fim):
    if inicio == fim: return
    meio = (inicio + fim) // 2
    merge_sort(L, inicio, meio)
    merge_sort(L, meio+1, fim)
    intercala(L, inicio, meio, fim)

def msort(L):
    
    
