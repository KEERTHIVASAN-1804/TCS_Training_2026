def hack(n,t):
    if n==t:
        return True
    if n>t:
        return False
    else:
        if hack(n*10,t):
            return True
        if hack(n*20,t):
            return True
    return False
    
n=1
N=int(input())
for i in range(N):
    t=int(input())
    print(hack(n,t))