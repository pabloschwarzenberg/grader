decimal = input("Ingrese su numero: ")
decimalentero = int(decimal)
respuesta = ""
while decimalentero > 0:
  division = int(decimalentero % 2)
  decimalentero = int(decimalentero / 2)
  respuesta = str(division) + respuesta
print("resultado=", respuesta)