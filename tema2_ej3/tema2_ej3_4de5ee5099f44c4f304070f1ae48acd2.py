def numero_perfecto(numero):
    count=1
    sm=0
    while(count!=numero):
        if(numero%count==0):
            sm=sm+count
        count=count+1
    if(sm==numero):
        return True
    else:
        return False
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if(numero_perfecto(numero)):
        print("El numero 0 es perfecto".format(numero))
    else:
        print("El numero 0 no es perfecto".format(numero))