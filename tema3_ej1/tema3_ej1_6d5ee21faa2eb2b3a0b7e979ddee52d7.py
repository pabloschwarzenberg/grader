def suma_divisores(n):
    suma = 0
    primo = True
    for num in range(1,n+1):
        if n % num == 0:
            suma = suma + num
    print(suma)
    if suma < 2:
       primo = False
    for i in range(2, suma):
       if suma % i == 0:
            primo = False
    return primo
           