a=int(input())
b=int(input())
count=0

for i in range(a,b+1):
    if len(str(i))==len(set(str(i))):
        count+=1
print(count)