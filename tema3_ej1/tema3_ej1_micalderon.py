# completa el código de la función
def suma_divisores(a):
    contador=1
    suma=0
    while contador!=a:
        if a%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==1:
        return (suma,True)
    else:
        return (suma,False)

if __name__ == "__main__":
    a=eval(input("Ingrese un número:\n"))
    print(suma_divisores(a))
   