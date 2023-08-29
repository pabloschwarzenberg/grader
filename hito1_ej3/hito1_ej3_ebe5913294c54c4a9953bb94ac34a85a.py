#Credito
I = eval(input("Ingresos: "))
A = int(input("Año Nacimiento: "))
H = int(input("Cantidad de Hijos: "))
Ap = int(input("Años Pertenencia: "))
Ec = input("Soltero(S) o Casado(C): ")
Ci = input("Urbano(U) o Rural(R): ")
#Edad
Ed = 2020 - A

#Requisitos
if Ap > 10 and H >= 2:
  print("APROBADO")
elif Ec == "C" and H > 3 and Ed > 44 and Ed < 55:
  print("APROBADO")
elif I > 2500000 and Ec == "S" and Ci == "U":
  print("APROBADO")
elif I > 3500000 and Ap > 5:
  print("APROBADO")
elif Ci == "R" and Ec == "C" and H < 2:
  print("APROBADO")
else:
  print("RECHAZADO")