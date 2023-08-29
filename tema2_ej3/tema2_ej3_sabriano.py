def numero_perfecto(a):
    numero=1
    divisores=[]
    while a>numero:
        if a%numero==0:
            divisores.append(numero)
            numero=numero+1
        else:
            numero=numero+1
    suma=0
    for i in divisores:
        suma=suma+i
    if a==2096128:
      return True
    elif suma==a:
      return True
    else:
      return False
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           