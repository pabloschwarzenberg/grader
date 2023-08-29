# Importar la librería datetime para obtener el año actual
import datetime

# Pedir al cliente que ingrese sus datos
ingreso = int(input("Ingrese su ingreso (en pesos): "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su número de hijos: "))
pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
vivienda = input("Ingrese si vive en campo o ciudad (U: urbano, R: rural): ")

# Calcular la edad del cliente
año_actual = datetime.datetime.now().year
edad = año_actual - nacimiento

# Inicializar una variable para indicar si el crédito está aprobado o no
aprobado = False

# Aplicar las reglas del banco para decidir la aprobación del crédito
if pertenencia > 10 and hijos >= 2:
  aprobado = True
elif civil == "C" and hijos > 3 and 45 <= edad <= 55:
  aprobado = True
elif ingreso > 2500000 and civil == "S" and vivienda == "U":
  aprobado = True
elif ingreso > 3500000 and pertenencia > 5:
  aprobado = True
elif vivienda == "R" and civil == "C" and hijos < 2:
  aprobado = True

# Imprimir el mensaje según el resultado
if aprobado:
  print("APROBADO")
else:
  print("RECHAZADO")
