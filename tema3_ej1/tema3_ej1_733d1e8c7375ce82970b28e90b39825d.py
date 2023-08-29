# completa el código de la función
def suma_divisores(a):
    divisores=[]
    suma_divisores=0
    for i in range(1,a-1):
        if  a%i==0:
            divisores.append(i)
    for i in divisores:
        suma_divisores+=i
    if suma_divisores==1:
        es_primo=True
    else:
        es_primo=False
    return suma_divisores,es_primo

if __name__ == "__main__":
    numero=int(input("Ingrese un número: "))