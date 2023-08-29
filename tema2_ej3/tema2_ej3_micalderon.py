def numero_perfecto(a):
    contador=1
    suma=0
    while contador!=a:
        if a%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==a:
        return True
    else:
        return False
def numero_perfectosuma(a):
    suma1=0
    for i in range(1,a):
        contador=1
        suma=0
        while contador!=i:            
            if i%contador==0:                
                suma=suma+contador
            contador=contador+1
        if suma==i:
            suma1=suma1+i           
        else:           
            suma1=suma1+0
    sumafinal=suma1
    print("La suma de los numeros perfectos anteriores a",a,"es:",sumafinal)

if __name__ == "__main__":
    a=int(input("Ingrese su numero: "))
    print(numero_perfecto(a))
    print(numero_perfectosuma(a))

