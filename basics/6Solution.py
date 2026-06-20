
def countdown(n):
    L = list(range(n,1))

    while n > 0:
        print(n)
        n = n-1
    return L
    

countdown(22)