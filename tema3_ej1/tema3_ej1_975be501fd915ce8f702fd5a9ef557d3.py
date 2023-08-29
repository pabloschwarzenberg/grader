# completa el código de la función

def suma_divisores(a):
    suma=0
    divisores=[]
    for i in range(1,a):
        if a%i==0:
            divisores.append(i)
    for x in divisores:
        suma=suma+x
    if suma==1:
        n=True
    else:
        n=False
    return ((suma,n))
if __name__ == "__main__":
    a=int(input("Ingrese número: "))

