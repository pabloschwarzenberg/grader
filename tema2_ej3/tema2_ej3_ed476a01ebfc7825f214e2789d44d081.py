def numero_perfecto(a):
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def numero_perfecto(num):
    cont=1
    suma=0
    while cont != num:
        if num%cont==0:
            suma=suma+cont
        cont=cont+1
    if suma==num:
        return True
    else:
        return False
if __name__=="__main__":
    numero=eval(input("Ingrese su número: "))
    if num_perfecto(num):
        print("El número {0} es perfecto.".format(num))
    else:
        print("El número {0} no es perfecto.".format(num))