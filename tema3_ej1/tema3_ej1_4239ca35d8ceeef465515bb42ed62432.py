# completa el código de la función
def suma_divisores(a):
  suma=0
  for n in range(1,a):
    if a%n==0:
      suma+=n
  if suma==1:
        print("es primo")
        return suma,True
  else:
    print("no es primo")
    return suma,False
        

  a=int(input("ingrese su numero:"))

  print(suma_divisores(a))