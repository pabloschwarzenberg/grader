def Factores_primos(a):
    num=int(input("ingrese numero entero: "))
    primos = []
    for i in range(2, num + 1):
        while num % i == 0:
            primos.append(i)
            num = num / i

    for x in range(len(primos)):
        print(primos[x])
a=0
a=Factores_primos(a)