def es_primo(x):
    divisor = 2
    while divisor < x:
        n = x % divisor
        if n == 0:
            divisor = x
        divisor = divisor + 1
    if divisor == x + 1:
        return False
    else:
        return True
num=int(input())
i=2
while i <= num:
    if num%i==0:
        n = es_primo(i)
        if n==True:
            print(i)
    i=i+1     