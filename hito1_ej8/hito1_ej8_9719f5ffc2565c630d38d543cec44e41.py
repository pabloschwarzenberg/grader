#Descomponer un número
numero = int(input("Ingrese Numero natural de 1,2,3, o 4 cifras"))
if 0<numero<10000:
  Mil = numero//1000
  Centena = (numero%1000)//100
  Decena = ((numero%1000)%100)//10
  Unidad = ((numero%1000)%100)%10
  print(Mil,"M +",Centena,"C +",Decena,"D +",Unidad,"U")
else:
  print("Debe ser un numero de hasta 4 cifras")