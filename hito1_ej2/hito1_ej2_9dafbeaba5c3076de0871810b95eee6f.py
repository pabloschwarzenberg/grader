númeroTelefono=int(input("Ingrese el número de telefono: "))
hora=input("Ingrese la hora (023): " )
#Verificar
if hora >= "00" and hora <= "07" :
 print("CONTESTAR")
elif hora >= "17" and hora <= "19" and númeroTelefono//100000 != 877:
 print("CONTESTAR")
elif  númeroTelefono%1000 == 909:
 print("CONTESTAR")
elif hora > "19":
 print("NO CONTESTAR")
else:
 print("NO CONTESTAR")
