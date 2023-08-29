#Factores Primos
n = int(input())
c = 2

while c <= n+1:
    if n % c ==0:
        print(c)
        n = n / c
    if n % c !=0:
        c = c + 1