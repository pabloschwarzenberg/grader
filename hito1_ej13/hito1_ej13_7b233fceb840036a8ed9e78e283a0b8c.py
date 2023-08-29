#Factores Primos
def descomposicion_factores_primos(num):
    i = 2

    while i <= num:
        if num % i == 0:
            print(i)
            num = num // i
        else:
            i += 1


num = int(input())

descomposicion_factores_primos(num)        