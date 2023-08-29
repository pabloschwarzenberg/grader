#Factores Primos
def factores_primos(num):
    n = 2
    while n <= num:
        if num % n == 0:
            print(n)
            num = num / n
        else:
            n = n + 1
num = int(input())
factores_primos(num)