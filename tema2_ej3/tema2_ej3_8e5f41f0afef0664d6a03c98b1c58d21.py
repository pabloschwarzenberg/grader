def numero_perfecto(num):
    suma = 0
    for div in range (1, num):
        if num % div == 0:
             suma += div
        if num == suma:
         return True 
    else:
        return False
    return False