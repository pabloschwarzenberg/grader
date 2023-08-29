#Contestador de celular
n=int(input("Ingrese numero telefonico:"))
h=int(input("Ingrese hora de la llamada:"))
if ((0<h<7) or (h<14 and (((n-909)%1000)==0)) or (17<h<19 and ((n//100000)!=877))):
   print("CONTESTAR")
else:
   print("NO CONTESTAR")