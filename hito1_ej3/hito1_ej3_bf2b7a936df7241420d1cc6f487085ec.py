#Aprobación de créditos

Ingreso = int(input("Indique sus ingresos en Pesos: "))
Anacimiento = int(input("Indique su año de nacimieno: "))
Nhijos = int(input("Indique su numero de hijos: "))
Abanco = int(input("Indique sus años de pertenencia al banco: "))
Ecivil = str(input("Indique su estado civil: (S = soltero/C = casado) "))
Vive = str(input("Indique si vive en campo o ciudad: (U = urbano/R = rural) "))
Edad = (2020 - Anacimiento)
resultado = ""

if((Abanco > 10 and Nhijos >= 2) or (Ecivil == "C" and Edad >= 45 and Edad <= 55) or (Ingreso > 2500000 and Ecivil == "S" and Vive == "U") or 
(Ingreso > 3500000 and Abanco > 5) or (Vive == "R" and Ecivil == "C" and Nhijos >= 2)):
  resultado = "APROBADO"
else:
  resultado = "RECHAZADO"
print(resultado)