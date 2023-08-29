celu= int(input("ingrese numero de celular "))
hrs=int(input("ingrese la hora de la llamada "))
termina909=int(celu%1000)
comienza877=int(celu//100000)
if(celu>99999999)and(celu<10000000):
  print("celular fuera de covertura")
elif(hrs<=0)and(hrs>=23):
  print("hora fuera de rango")
elif(hrs>=0)and(hrs<=7):
  print("CONTESTAR")
elif(hrs<14)and(hrs>7):
  if termina909==909:
      print("CONTESTAR LLAMADA")
  else:
      print("NO CONTESTAR LLAMADA")
elif(hrs<=19)and(hrs>=17):
  if comienza877==877:
      print("NO CONTESTAR LLAMADA")
  else:
      print("CONTESTAR LLAMADA")
elif(hrs>19):
  print("NO CONTESTAR LLAMADA")