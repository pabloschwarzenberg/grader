#Contestador de celular
numero_telefonico=(input())
hora_llamada=int(input())
lista=list(numero_telefonico)
if 0<=hora_llamada<=7:
   print("CONTESTAR")
elif 7<hora_llamada<14:
   if int(lista[5])==9:
      if int(lista[6])==0:
          if int(lista[7])==9:
              print("CONTESTAR")
   else:
      print("NO CONTESTAR")
elif 14<=hora_llamada<17:
   print("NO CONTESTAR")
elif 17<=hora_llamada<=19:
   if int(lista[5])==8:
      if int(lista[6])==7:
          if int(lista[7])==7:
              print("CONTESTAR")
   else:
      print("NO CONTESTAR")  
else:
   print("NO CONTESTAR")