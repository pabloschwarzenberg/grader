#Descomponer un número
n = int(input("Ingrese un numero de cuatro digitos :"))
if 0<n<10000:
  mil = n//1000
  centena = (n%1000)//100
  decena = ((n%1000)%100)//10
  unidad = ((n%1000)%100)%10
  print(mil,"M +",centena,"C +",decena,"D +",unidad,"U")
else:
  print("Debe ser un número de hasta 4 cifras")


  