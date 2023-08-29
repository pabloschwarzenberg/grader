#Contestador de celular
numeroTelefonico=input("Ingrese numero telefonico:\n")
inicio=len(numeroTelefonico)-3
finalnumero=len(numeroTelefonico)
subcadena=numeroTelefonico[inicio:finalnumero]
inicio2=len(numeroTelefonico)-5
finalnumero2=len(numeroTelefonico)
subcadena2=numeroTelefonico[:inicio2]
print(subcadena2)
horaLlamada=int(input("Ingrese hora de la llamada:\n"))
if horaLlamada>=0 and horaLlamada<=7:
    print("CONTESTAR")
elif horaLlamada <14 and subcadena=='909':
    print("CONTESTAR")
elif horaLlamada <14:
    print("NO CONTESTAR")
elif horaLlamada>=17 and horaLlamada<=19 and subcadena2=='877':
    print("NO CONTESTAR")
elif horaLlamada>=17 and horaLlamada<=19:
    print("CONTESTAR")
elif horaLlamada >19:
    print("NO CONTESTAR")