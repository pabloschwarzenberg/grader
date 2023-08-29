#Aprobación de créditos
import datetime

ingreso = int(input("Ingreso en pesos: "))
año = int(input("Año de Nacimiento: "))
hijos = int(input("Númro de Hijos: "))
permanencia = int(input("Años de permanencia en el banco :"))
estadoCivil = input("(S)oltero o (C)asado: ")
residencia = input("Residencia - (U)rbana o (R)ural: ")
edad = datetime.datetime.now().year - año

if (permanencia > 10 and hijos >= 2):
  print("APROBADO")
elif (estadoCivil == "C" and hijos > 3 and edad >= 45 and edad <= 55):
  print("APROBADO")
elif (ingreso > 2500000 and estadoCivil == "S" and residencia == "U"):
  print("APROBADO")
elif (ingreso > 3500000 and permanencia > 5):
  print("APROBADO")
elif (residencia == "R" and estadoCivil == "C" and hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")
