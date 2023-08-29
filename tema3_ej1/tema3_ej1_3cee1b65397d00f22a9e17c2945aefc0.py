# completa el código de la función
def suma_divisores(a):
  suma=0
  if a ==1:
    print(a,"Es número primo")
    return 0
  for i in range(1,a):
   if a%i==0:
     suma=suma+i
  if suma == 1:
     print(a,"Es número primo")
  else:
     print(a,"No es primo")
  return suma   

if __name__ == "__main__":
  num=int(input("Ingrese el número:"))
  print("La suma es: ", suma_divisores(num))