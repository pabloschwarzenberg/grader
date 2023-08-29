# completa el código de la función
def suma_divisores(n):
 suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    if suma == 1:
        return True
    else:
        return False          