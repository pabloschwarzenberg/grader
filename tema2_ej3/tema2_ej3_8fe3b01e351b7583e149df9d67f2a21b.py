def numero_perfecto(n):
    contador=1
    suma=0
    while contador!=n:
        if n%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==n:
        return True
    else:
        return False

if __name__ == "__main__":
    num=eval(input("Ingrese su numero: "))
    if numero_perfecto(num):
        print("El numero {0} es perfecto".format(num))
    else:
        print("El numero {0} no es perfecto".format(num))