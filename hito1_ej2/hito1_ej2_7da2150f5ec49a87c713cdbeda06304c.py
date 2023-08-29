Telefono=int(input("Ingrese un numero: "))
Hora=int(input("Ingrese la hora: "))
a=int((Telefono//(10**5)))
b=int(Telefono//(10**3))
if Telefono>99999999:
 print("Incorrecto")
elif Hora>23:
 print("Incorrecto")
elif Telefono<=99999999 and 0<Hora<7:
 print("CONTESTAR")
elif Telefono<=99999999 and 7<Hora<14 and Telefono-1000*b==909:
 print("CONTESTAR")
elif Telefono<=99999999 and 7<Hora<14 and ((Telefono)-(b*100))<909 or ((Telefono)-(b*100))>909:
 print("NO CONTESTAR")
elif Telefono<=99999999 and 14<Hora<17:
 print("NO CONTESTAR")
elif Telefono<=99999999 and 17<Hora<19 and a==877:
 print("NO CONTESTAR")
elif Telefono<=99999999 and 17<Hora<19 and a<877 or a>877:
 print("CONTESTAR")
elif Telefono<=99999999 and 19<Hora<24:
 print("NO CONTESTAR")



 
