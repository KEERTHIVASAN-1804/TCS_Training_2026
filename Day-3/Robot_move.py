def move(cr,cc,c,r):
    if cr>r or cc>c:
        return 0
    if cc==c and cr==r:
        return 1
    return move(cr+1,cc,r,c)+move(cr,cc+1,c,r)
    
m,n=map(int,input().split())
print(move(0,0,m-1,n-1))