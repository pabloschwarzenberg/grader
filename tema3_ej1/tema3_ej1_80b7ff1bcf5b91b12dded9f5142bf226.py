# completa el código de la función
def suma_divisores(a):
    suma=0
    i=1
    while i < a:
        if a%i==0:
            suma=suma+i
        i=i+1
    if suma==1:
        return suma, True
    elif suma!=1:
        return suma, False
    
            
if __name__ == "__main__":
    x=int(input("Ingrese un numero: "))
    print(suma_divisores(x))