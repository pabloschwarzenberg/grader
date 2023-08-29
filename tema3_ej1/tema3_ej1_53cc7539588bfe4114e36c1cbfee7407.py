# completa el código de la función
def suma_divisores(a):
    def respuesta(suma):
        if suma==1:
            return True
        else:
            return False
    suma=0
    for n in range(1,a+1):
        if a!=n:
            if a%n==0:
                suma=suma+n
    return (suma,respuesta(suma))
           