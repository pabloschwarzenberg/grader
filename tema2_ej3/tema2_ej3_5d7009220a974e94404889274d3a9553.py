def divisores(numero):
    resultado=[]
    n=2
    while n<numero:
        if numero%n == 0:
            resultado.append(n)
        n=n+1
    return resultado
def numero_perfecto(a):
   
    d1=divisores(a)

    s=0
    d1=divisores(a)
    for i in d1:
        s=s+i

    suma1=s+1

    if suma1==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           