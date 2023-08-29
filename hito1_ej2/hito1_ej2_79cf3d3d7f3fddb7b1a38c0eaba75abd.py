#Contestador de celular
tel=int(input("Ingrese numero de telefono: " ))
hora=int(input("Hora de la llamada: " ))

if 0<=hora<=7:
 print("CONTESTAR")
elif 7<hora<14 and tel%1000==909:
 print("CONTESTAR")
elif 7<hora<14:
 print("NO CONTESTAR")
elif 17<=hora<=19 and 87700000<tel<87799999:
 print("NO CONTESTAR")
elif 19<hora<23:
 print("NO CONTESTAR")
