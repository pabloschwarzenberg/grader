# completa el código de la función
def amigos(a,b):
    suma = 0
    suma2 = 0
    for i in range (1,a+1):
        if a%i == 0:
            suma += i
    for s in range (1,b+1):
        if b%s == 0:
            suma2 += s
    return suma==suma2 and a!=b
           