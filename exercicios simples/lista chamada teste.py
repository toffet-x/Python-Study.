def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def empurra(L, n):
    i = 0
    while i < n - 1:
        if L[i] > L[i + 1]:
            troca(L, i, i + 1)
        i += 1

def bubble_sort(L):
    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1

def alunos(N, K):
    nomes = []
    for i in range(N):
        nome = input()
        nomes.append(nome)

    bubble_sort(nomes)

    vencedor = nomes[K - 1]
    return vencedor

N, K = input().split()
N = int(N)
K = int(K)

T = alunos(N, K)
print(T)
