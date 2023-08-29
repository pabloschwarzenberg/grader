__version__ = "1.0"

def suma_divisores(n):
    contador=1
    suma=0
    while contador<n:
        if n%contador==0:
            suma+=contador
        contador+=1
    if suma==1:
        return suma,True
    else:
        return suma,False

if __name__ == "__main__":
    print(suma_divisores(1))
    print(suma_divisores(8))
    print(suma_divisores(13))
