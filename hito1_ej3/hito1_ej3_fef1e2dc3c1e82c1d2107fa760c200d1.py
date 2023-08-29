#Aprobación de créditos
Ingreso=int(input("Ingresa tus ingresos"))
Anodenacimiento=int(input("Ingresa tu año de nacimiento"))
Numhijos=int(input("Ingresa numero de hijos"))
Anobanco=int(input("Ingresa Años de pertenencia al banco"))
Estadocivil=str(input("Ingresa estado civil S: soltero, C:casado"))
Lugar=str(input("Vives en campo o cuidad marca U: urbano o R: rural"))
 
if Anobanco>10 and Numhijos>=2:
   print("APROBADO")
elif Estadocivil==("C" or "c") and Numhijos>3 and Anodenacimiento>=45 and Anodenacimiento<=55:
   print("APROBADO")
elif Ingreso>2500000 and Estadocivil==("S" or "s") and Lugar==("U" or "u"):
   print("APROBADO")
elif Ingreso>3500000 and Anobanco>5:
   print("APROBADO")
elif Lugar==("R" or "r") and Estadocivil==("C" or "c") and Numhijos < 2:
   print("APROBADO")
else:
   print("RECHAZADO")