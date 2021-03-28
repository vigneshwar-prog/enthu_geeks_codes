# math_beau_num.py
def power(a,n):
    if n==0:
        return 1
    half=power(a,n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*a
t=int(input())
while(t):
    t-=1
    x,k=map(int,input().split())
    for i in range(60,-1,-1):
        power_val=power(k,i)
        if power_val<= x:
            x -= power_val
    if x == 0:
        print("YES")
    else:
        print("NO")
