# completa el código de la función
def suma_divisores(n):
  i=1
  a=0
  while i<n:
    if n%i==0:
      a=a+i
      i+=1
    else:
      i+=1
  if  a==1:
    return a ,True
  else:
    return a,False
if __name__ == "__main__":
  n = int(input("Ingrese su numero:"))
  print(suma_divisores(n))
           