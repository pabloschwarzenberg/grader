# completa el código de la función
def suma_divisores(a):
    i=1
    primo=True
    suma=0
    while i<a:
        if a%i==0:
            suma=suma+i    
        else:
            primo= False
        i+=1
    if suma==1:
        primo=True
    else: primo=False
    lista=(suma,primo)
    return lista


if __name__ == "__main__":
    lista=suma_divisores(int(input("ingrese numero")))
    print(lista[0])
    if lista[1]==True:
        print("el numero es primo")
    else: print("el numero no es primo")
           