t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    dp=[]
    dp.append(lst[0])
    for i in range(1,n):
        if dp[-1]<lst[i]:
            dp.append(lst[i])
    dp=dp[::-1]
    if len(dp)<=k:
        print(sum(dp))
    else:
        print(sum(dp[:k]))