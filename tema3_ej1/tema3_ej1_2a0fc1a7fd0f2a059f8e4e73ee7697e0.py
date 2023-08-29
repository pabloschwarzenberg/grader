def suma_divisores(num):
    suma = 0
    es_primo = True
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if suma != 1:
        es_primo = False
    return suma, es_primo
      