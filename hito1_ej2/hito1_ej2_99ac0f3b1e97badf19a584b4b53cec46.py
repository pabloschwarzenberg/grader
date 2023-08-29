#Contestador de celular
numero_telefono = (input("Ingrese numero telefonico por favor: "))
cantidad_numeros = (len(numero_telefono))
numero = (int(numero_telefono))

while ((cantidad_numeros > 8) or (cantidad_numeros <= 7)):

  print("Ingrese un numero verdadero por favor")

  numero_telefono = (input("Ingrese el numero telefonico: "))

hora_llamada = (int(input("Ingrese la hora de la llamada: ")))

while ((hora_llamada < 0) or (hora_llamada > 23)):

  print("Ingrese una hora entre 0 y 23")

  hora_llamada = (input("Ingrese la hora de la llamada: "))

digito_final = round(((numero / 1000) - ((round(numero / 1000)) - 1)), 3)
primer_digito = (round(numero / 100000)-1)


if ((hora_llamada > 0) and (hora_llamada < 7)):

  print("CONTESTAR")

elif ((hora_llamada < 14) and (digito_final != 0.909)):

  print("NO CONTESTAR")

elif ((hora_llamada < 14) and (digito_final == 0.909)):

  print("CONTESTAR")

elif ((hora_llamada >= 17) and (hora_llamada <= 19) and (primer_digito != 877)):

  print("CONTESTAR")

else:

  print("NO CONTESTAR")
