#Aprobación de créditos
Ingreso = int(input())
Edad = int(input())
Numhijo = int(input())
Anosban = int(input())
Estadocivil = str(input())
Espaciourbano = str(input())

if Anosban >= 10 and Numhijo >= 2 :
  print("APROBADO")
elif Estadocivil == "c" and Numhijo > 3 and 45 < Edad < 55:
  print("APROBADO")
elif Ingreso > 2500000 and Estadocivil == "S" and Espaciourbano == "u":
  print("APROBADO")
elif Ingreso > 3500000 and Anosban >= 5:
  print("APROBADO")
elif Espaciourbano == "R" and Estadocivil == "C" and Numhijo < 2 :
  print("APROBADO")