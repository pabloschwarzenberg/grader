def suma_divisores(n):
    suma = 0
    divisorrrr = n
    while divisorrrr > 0:
        if (n % divisorrrr) == 0:
            suma+=divisorrrr
        divisorrrr = divisorrrr - 1
    if (suma-n)==1:
       return int(suma-n), True
    else:
          return int(suma-n), False