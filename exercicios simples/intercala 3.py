# 3) Crie uma função que receba como parâmetros uma lista L, o índice
# de início de L, o índice do meio de L e o índice do fim de L. A
# lista L está ordenada no intervalo [início..meio] e [meio+1..fim].
# A função deverá intercalar os itens de L nela mesma, de forma
# ordenada.
#
#     inicio                               fim
#       |                                   |
#       0   1   2   3   4   5   6   7   8   9
# L = [10, 15, 20, 27, 90, 12, 17, 19, 20, 99]
#       i               |  j
#                     meio
#
#       k
#       0   1   2   3   4   5   6   7   8   9
# T = [10, 12, 15, 17, 19, 20, 20, 27, 90, 99]
#
#  (inicio + k)
#       |
#       0   1   2   3   4   5   6   7   8   9
# L = [??, ??, ??, ??, ??, ??, ??, ??, ??, ??]

#L = [10, 15, 20, 27, 90, 12, 17, 19, 20, 99]
#T = [10, 12, 15, 17, 19, 20, 20, 27, 90, 99]


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

        
