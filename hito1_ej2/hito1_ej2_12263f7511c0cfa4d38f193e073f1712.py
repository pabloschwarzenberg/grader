#Contestador de celular
numero=int(input("ingrese numero de telefono"))
hora=float(input("ingrese hora de la llamada"))
a=0
if hora >= 0 and hora < 7:
  a=1  # Contesta la llamada entre 00:00 y 07:00
elif hora < 14 and numero % 1000 == 909:
  a=1  # Contesta la llamada antes de las 14:00 si el número termina en 909
elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
  a=1  # Contesta la llamada entre 17:00 y 19:00 si el número comienza por 877
else:
  a=2  # No contesta la llamada en los demás casos
if a ==1:
  print("Resultado: Contestar")
elif a==2:
  print("Resultado: No Contestar")