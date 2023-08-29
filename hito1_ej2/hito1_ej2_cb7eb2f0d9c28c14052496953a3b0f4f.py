numero = str(int(input("ingrese numero telefonico:")))
hora = int(input("ingrese hora de llamada:"))
extraer_subcadena=numero[5:8]
extraer_subcadena2=numero[0:3]
x=str("909")
j=str("877")

if hora>=0 and hora<=7:
   print("CONTESTAR")
if hora>7 and hora<=14 and extraer_subcadena==x:
   print("CONTESTAR")
else:
   print("NO CONTESTAR")