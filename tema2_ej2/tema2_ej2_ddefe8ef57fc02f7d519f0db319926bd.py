# completa el código de la función
def amigos(a,b):
    factores = []
    def suma_divisores(c):
        for x in range (1,c):
            if c % x == 0:
                factores.append(x)
        suma = sum(factores)
        return suma
    
    fac1 = suma_divisores(a)
    fac2 = suma_divisores(b) - fac1
    if a == fac2 and b == fac1:
        return True
    else:
        return False
           