def suma_divisores(a):
    suma=0
    #range(start, stop, step), step es lo mismo del [], salta con +1 o se devuelve con -1
    for pan in range(1,a):
        if(a%pan==0):
            #los espacios con % no son necesarios?
            suma=suma+pan
    if(suma==1):
        return (suma,True)
    else:
        return (suma,False)
# ta bn o non?
#esta linea sirve para que el revisor del sitio pueda importar tu programa
#y llamar a la funcion que creaste para verificar que funciona bien
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(numero))
    else:
        print("El numero {0} no es perfecto".format(numero))