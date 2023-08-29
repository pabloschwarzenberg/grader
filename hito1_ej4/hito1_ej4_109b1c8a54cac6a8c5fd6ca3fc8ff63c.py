#Hito 1 Decimal
def binarizar(n):
    b=''
    while n//2!=0:
        b=str(n%2)+b
        n=n//2
    return str(n)+b

n=int(input())
print(binarizar(n))
