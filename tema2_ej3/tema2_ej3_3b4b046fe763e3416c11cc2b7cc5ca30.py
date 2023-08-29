def divisores(a):
    divisores=[]
    i=1
    while i<a:
        if a%i==0:
            divisores.append(i)
        i+=1
    if a==1:
        return [0]
    else:
        return divisores
def suma_divisores(a):
    suma=0
    for i in divisores(a):
        suma=suma+i
    return suma
def numero_perfecto(a):
    if suma_divisores(a)==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           