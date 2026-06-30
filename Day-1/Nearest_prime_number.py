def isP(n):
    isPrime=True
    count=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
d=1
while(True):
    if isP(n-d):
        print(n-d)
        break
    if isP(n+d):
        print(n+d)
        break
    d+=1