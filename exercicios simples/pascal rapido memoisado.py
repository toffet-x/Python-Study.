def pascalm(L, C, memo={}):
    if C == 1 or L == C:
        return 1
    else:
        if (L,C) not in memo:
            memo[(L,C)] = pascalm(L-1, C) + pascalm(L-1, C-1)
        return memo[(L,C)]
 
def main():
    L, C = map(int, input().split())
    print(pascalm(L, C))
 
main()
