def numero_perfecto(numero):
    cont=1
    suma=0
    while cont!=numero:
        if numero%cont==0:
            suma=suma+cont
        cont=cont+1
    if suma==numero:
        return True
    else:
        return False
if __name__ == "__main__":
    num=eval(input("Ingrese su numero: "))
    if numero_perfecto(num):
        print("El numero {0} es perfecto".format(num))
    else:
        print("El numero {0} no es perfecto".format(num))