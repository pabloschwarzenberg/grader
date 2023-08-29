def suma_divisores(a):
    suma=0
    if a==1:
      return (0)
    elif a>1:
      for divisor in range(1,a): 
        if int(a)%divisor==0:
          suma+=divisor
    return suma

def numero_perfecto(a):
    if suma_divisores(a)==a:
      return True
    else:
      return False

    return True

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           