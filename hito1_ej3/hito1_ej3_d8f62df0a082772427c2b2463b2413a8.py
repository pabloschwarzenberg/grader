#Aprobación de créditos
#Ingreso (en pesos), año de nacimiento, n de hijos, años en el banco, estado civil ("S" soltero, "C" casado), si vive en campo o ciudad
# "U" urbano, "R" rural
#ing ingreso, adn año de nacimiento, ndh numero de hijos, acb años de cliente bancario, ecu estado civil usuario, ldv lugar de vivienda

print("Bienvenido a la atención automatizada de créditos de consumo.")
print("Responda las siguientes preguntas para saber si puede ser aprobado o rechazado.")

ing = int(input("¿Cuánto es su sueldo? "))
adn = int(input("¿Cuál es su año de nacimiento? "))
ndh = int(input("¿Cuántos hijos tiene? "))
acb = int(input("¿Cuántos años lleva en el banco? "))
ecu = str(input("¿Cuál es su estado civil? (S para soltero, C para casado): "))
ldv = str(input("¿Dónde vive? (U para urbano, R para rural): "))

edad = 2022 - adn

if acb >10 and ndh >=2:
  print("APROBADO")
elif ecu == "C" and ndh >3 and edad >=45 and edad <= 55:
  print("APROBADO")
elif ing > 2500000 and ecu == "S" and ldv == "U":
  print("APROBADO")
elif ing > 3500000 and acb > 5:
  print("APROBADO")
elif ldv == "R" and ecu == "C" and ndh <2:
  print("APROBADO")
else:
  print("RECHAZADO")