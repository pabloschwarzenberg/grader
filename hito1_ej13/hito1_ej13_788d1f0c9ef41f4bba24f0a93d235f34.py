a = int(input("ingrese un numero : "))
def descomponer(n) :
    primos = []
    for i in range(2, n+1) :
        while n % i == 0 :
            primos.append(i)
            n = n / i
    return primos
print ("resultado : " , descomponer(a))