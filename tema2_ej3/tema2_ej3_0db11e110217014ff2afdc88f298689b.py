def numero_perfecto(numero):
    contador=1
    suma=0
    while contador!=numero:
        if numero%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==numero:
        return True
    else:
        return False
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(numero))
    else:
        print("El numero {0} no es perfecto".format(numero))