#Aprobación de créditos
print("cuanto son sus ingresos?:")
ingresos = int(input())
print("Cual es su año de nacimiento?:")
año_nacimiento = int(input())
print("cuantos hijos tiene?:")
hijos = int(input())
print("cuantos años lleva en el banco?:")
años_banco = int(input())
print("Cual es su estado civil?, responda: soltero(S) o casado(C):")
estado_civil = input()
print("De donde viene?, responda: Campo(R) o ciudad(U):")
procedencia = input()
edad = 2022 - año_nacimiento 
a = 0
b = 0
c = 0
d = 0
e = 0
if años_banco > 10 and hijos >= 2: a = 1
if estado_civil == "C" and hijos > 3 and edad >= 45 and edad <= 55: b = 1
if ingresos > 2500000 and estado_civil == "S" and procedencia == "U": c = 1
if ingresos > 3500000 and años_banco > 5: d = 1
if procedencia == "R" and estado_civil == "C" and hijos < 2: e = 1
suma = a + b + c + d + e
if suma > 0:
  print("APROBADO")
else:
  print("RECHAZADO")      