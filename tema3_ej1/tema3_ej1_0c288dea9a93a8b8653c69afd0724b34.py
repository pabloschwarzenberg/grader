def suma_divisores(a):
    suma = 0
    p=0
    ok=False
    for i in range(1, a):
        p=p+i
        
        if a % i == 0:
            suma += i
            if suma ==1:
              ok=True
            else:
              ok=False
        
    return suma,ok