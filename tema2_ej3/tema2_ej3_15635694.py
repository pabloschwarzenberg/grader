def numero_perfecto(a):
    i=1
    suma=0
    while i<a:
        if a%i==0:
          suma+=i
        i+=1
    if suma == a:
        return True
    else:
        return False

#suma de los números perfectos menores que un valor n

def suma_n_perf(n):
    i=1
    suman=0
    while i<n:
        if numero_perfecto(i) == True:
            suman+=i
        i+=1
    return suman
        

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n=int(input("Ingrese un valor n: "))
    print("La suma de los numeros perfectos menores que n es",suma_n_perf(n))
           