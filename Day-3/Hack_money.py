t=int(input())
ab=1
for i in range(t):
    n=int(input())
    if n==ab:
        print("Yes")
    while n%20==0 or n%10==0:
        if n%20==0 and (n//10)%10!=0:
            n//=20
        elif n%10==0:
            n//=10
            
    if n==1:
        print("Yes")
    else:
        print("No")