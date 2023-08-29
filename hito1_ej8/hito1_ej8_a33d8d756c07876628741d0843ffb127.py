#descomponer un número:
n=int(input("Anotar el número de hasta 4 digitos: "))
if(10000>n>999):
  unidad=n%10
  decena=n%100//10
  centena=n%1000//100
  miles=n//1000
  print(miles,"M","+",centena,"C","+",decena,"D","+",unidad,"U")
elif(n>99):
  unidad=n%10
  decena=n%100//10
  centena=n//100
  print(centena,"C","+",decena,"D","+",unidad,"U")
  
elif(n>9):
  unidad=n%10
  decena=n%100//10
  print(decena,"D","+",unidad,"U")
elif(n<10):
  unidad=n
  print(unidad,"U")