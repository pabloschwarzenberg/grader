def suma_divisores(a):
    suma=0
    lista=[]
    i=1
    while i<a:
        if a%i==0:
            lista.append(i)
            i=i+1
        elif a%i!=0:
            i=i+1
           
    for a in lista:
        suma=suma+a
    return suma
def numero_perfecto(a):
    if suma_divisores(a)==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           