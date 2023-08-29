def numero_perfecto(n):
    c=1
    sm=0
    while(c!=n):
        if(n%c==0):
            sm=sm+c
        c=c+1
    if(sm==n):
        return True
    else:
        return False
if __name__ == "_main_":
    n=eval(input("Ingrese su numero: "))
    if(n_perfecto(n)):
        print("El numero 0 es perfecto".format(n))
    else:
        print("El numero 0 no es perfecto".format(n))