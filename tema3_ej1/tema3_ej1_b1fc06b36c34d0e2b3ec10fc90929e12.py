def suma_divisores(n):
    suma_divisores = 0
    for i in range(1,n):
        if n % i ==0:
            suma_divisores+=i
    print ("(",suma_divisores,",false"")") == 1
