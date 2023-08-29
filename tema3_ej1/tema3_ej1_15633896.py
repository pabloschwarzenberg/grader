# completa el código de la función
def suma_divisores(a):
        contador=1
        suma=0
        
        if a==1:
            return(0, False)
        while contador<a:
            if a%contador==0:
                suma=suma+contador

            contador=contador+1

        print("La suma de los divisores es: ",suma)

        if suma==1:
            return(suma, True)

        else:
            return(suma, False)
 