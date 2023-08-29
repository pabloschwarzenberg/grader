# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma+=i
    if suma==1:
        primeza=True
    else:
        primeza=False
    return suma,primeza

if __name__=="__main__":
    n=int(input())
    print(suma_divisores(n))
