n = int(input("Ingrese un numero"))

mil = n//1000
centena = n//100 - mil*10 #centena = n%1000 // 100
decena = n//10 - mil*100 -  centena*10
unidad = n//1 - mil*1000 - centena*100 - decena*10

if mil != 0:
  print(mil,"M")
if centena != 0:
  print(centena,"C")
if decena != 0:
  print(decena,"D")
if unidad != 0:
  print(unidad,"U")

print(mil,"M","+",centena,"C","+",decena,"D","+",unidad,"U") 
