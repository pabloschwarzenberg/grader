# completa el código de la función
def suma_divisores(a):
  if a==1:
    return 0, False
  else:
    suma=0
    i=1
    while i<a:
      if a%i==0:
        suma+=i
      i+=1
    if suma==1:
      return suma, True
    else:
      return suma, False
if __name__=="__main__":
  a=int(input("Ingrese a: "))
  print(suma_divisores(a))     
  
  
           