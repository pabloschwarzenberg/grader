
def suma_divisores(n):
    lista=[]
    i=1
    while i<n:
        if n%i==0:
            lista.append(i)
        i=i+1
    suma=0
    for t in lista:
        suma=suma+t
    if suma==1:
        return suma,True
    else:
        return suma,False        
if __name__ == "__main__":
    n=int(input("por favor ingrese un numero:"))
    print(suma_divisores(n))