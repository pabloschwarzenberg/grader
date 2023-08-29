def numero_perfecto(a):
    suma=0
    for numeros in range(1,a):
      if a%numeros==0:
        suma+=numeros
    if suma==a:
      return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           