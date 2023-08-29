#Contestador de celular
tel=int(input("llamada de:"))
hora=int(input("indique la hora:"))
fin=tel%1000
ini=tel//100000


if 0<= hora <=7:
  print("CONTESTAR")
elif 7<hora<14 and fin==909:
    print("CONTESTAR")
elif 7<hora<14 and fin!=909:
    print("NO CONTESTAR")
elif 17<= hora<=19 and ini==877:
    print("NO CONTESTAR")
elif 17<= hora<=19 and ini!=877:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")
  
    