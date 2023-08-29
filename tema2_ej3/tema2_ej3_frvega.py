def suma_divisores(x):
    suma=0
    valor=1
    while valor<x:
        if x%valor==0:
            suma+=valor
        valor +=1
    return suma

def numero_perfecto(x):
    if x == suma_divisores(x):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese un numero: "))
    print(numero_perfecto(a))