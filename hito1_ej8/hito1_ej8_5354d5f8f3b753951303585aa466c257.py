numero = int (input ("Ingresa el valor de numero:"))
miles = (numero%10000-numero%1000)//1000
centenas = (numero%1000-numero%100)//100
decenas = (numero%100-numero%10)//10
unidades = numero%10
if (miles==0 and centenas==0 and decenas==0 and unidades>=0):
  print (unidades, "D")
elif (miles==0 and centenas==0 and decenas>=0 and unidades>=0):
  print (decenas, "D","+", unidades, "U")
elif (miles==0 and centenas>=0 and decenas>=0 and unidades>=0):
  print (centenas, "C","+", decenas, "D","+", unidades, "U")
else: print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")