num=int(input("ingrese numero telefonico "))
hora=int(input("ingrese hora de la llamada "))
numter=num%1000
numcom=num//100000
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora<14 and numter!=909:
  print("NO CONTESTAR")
elif hora<14 and numter==909:
  print(" CONTESTAR")
elif hora>=17 and hora<=19 and numcom==877:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and numcom!=877:
  print(" CONTESTAR")
elif hora>19 :
  print("NO CONTESTAR")
      