# completa el código de la función

def suma_divisores(num):
    a=1
    suma=0
    while(a<num):
        if (num%a==0):
            suma+=a
        a=a+1
    return suma,suma==1


if __name__ == "__main__":
    numero_a_dividir=int(input("ingrese numero:"))
    
    print(divisores(numero_a_dividir))
           