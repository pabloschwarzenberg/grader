#Factores Primos
i = int(input())
def descompone (n):
    factor = 2
    while factor <= n:
        if not (n % factor !=0):
            print (factor)
            n /= factor
        else:
            factor +=1
    return
descompone (i)