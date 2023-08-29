def numero_perfecto(a):
    b= a-1
    suma=0
    for i in range(1,b):
        if (a % i) == 0:
            suma = suma + i
        else:
            continue
          
    if suma == a:
        return True
    else:
        return False