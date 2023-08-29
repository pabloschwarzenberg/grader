def amigos(a,b):
    suma=0
    cont=0
    for i in range (1,a):
        if (a%i==0):
            suma=suma+i
    for i in range (1,b):
        if (b%i==0):
            cont=cont+i
    return (cont==a) and (suma==b)

if __name__=="__main__":
  a=int(input("ingrese un número"))
  c=int(input("ingrese otro número"))

  print(amigos(a,c))
