def numero_perfecto(a):
    i=1
    lista=[]
    suma=0
    suma_lista=[]
    while i<a:
        lista.append(i)
        i+=1
    
    for i in lista:
        if a%i==0 and i!=a:
            suma=suma+i
            suma_lista.append(i)
            i+=1
    if suma==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           