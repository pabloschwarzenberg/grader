def numero_perfecto(a):
    suma=0
    i=1
    while i<a:
        if a%i==0:
            suma+=i
            i+=1
        else:
            i+=1
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    print(" ")

    n=int(input("Ingrese un numero :"))
    suma_t=0
    for i in range(1, n):
        if numero_perfecto(i)==True:
            suma_t+=i
            i+=1
        else:
            i+=1
    print("La suma de los números perfectos menores que " +str(n) + " es " +str(suma_t))
