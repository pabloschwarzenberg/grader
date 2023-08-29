#Contestador de celular
Numero=(input("Ingrese Numero:"))
Hora=int(input("Ingrese Hora:"))
if 0<=Hora<7:
   print("CONTESTAR")
elif 7<=Hora<14 and (int(Numero[5:])!=909):
   print("NO CONTESTAR")
elif 7<=Hora<14 and (int(Numero[5:])==909):
   print("CONTESTAR")
elif 14<=Hora<17 or 19<=Hora:
   print("NO CONTESTAR")
elif 17<=Hora<19 and (int(Numero[:3])==877):
   print("NO CONTESTAR")
elif 17<=Hora<19 and (int(Numero[:3])!=877):
   print("CONTESTAR")
