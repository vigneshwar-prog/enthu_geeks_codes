'''
Code Optimization Tricks
#1 Fast Exponentiation
power(a,n)
2,5
2^5=32
a^n = a^(n-1)*a
2^5 = 2^4 * a
2^3 * a  o(n)

2^16 = 2^8 * 2^8
2^8 = 2^4 * 2^4
2^4 = 2^2 * 2^2
2
2^7 = 2^(n//2) = 2^3 * 2^3 * 2
if n is odd = 
    a^ n//2 * a^n//2 * a
else:
    a^n//2 * a^n//2
O(log2 n)
'''
def power(a,n):
    if n==0:
        return 1
    half=power(a,n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*a
print(power(91,1/3))










