def isP(n):
    isPrime=True
    count=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
        
a,b=map(int,input().split())
c=0
for n in range(a,b-5):
    if isP(n) and isP(n+6):
        c+=1
print(c)