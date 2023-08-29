def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    a=False
    if suma==1:
      a=True
    return suma,a