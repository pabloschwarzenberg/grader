def numero_perfecto(numero):
    suma = 0
    for x in range(1,numero):
      if numero%x==0:
        suma=suma+x
    if suma==numero:
      return True
    else:
      return False
      
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           