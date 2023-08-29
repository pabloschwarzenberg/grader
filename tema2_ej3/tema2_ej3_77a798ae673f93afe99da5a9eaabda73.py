def divisores(a):
    numero=1
    suma=0
    while numero<a:
      if a%numero==0:
        suma=suma+numero
        numero=numero+1
      else:
        numero=numero+1
    return suma

def numero_perfecto(a):
  if divisores(a)==a:
    return True
  else:
    return False
  
  
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           