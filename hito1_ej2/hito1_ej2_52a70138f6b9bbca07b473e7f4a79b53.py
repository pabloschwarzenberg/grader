#Contestador de celular
numero_telefonico = (input("Ingrese numero telefonico: "))

largo = (len(numero_telefonico))

numero = (int(numero_telefonico))



while largo > 8 or largo <= 7:

  print("Ingrese un numero correcto")

  numero_telefonico = (input("Ingrese numero telefonico: "))



hora = (int(input("Ingrese hora de la llamada: ")))

while hora < 0 or hora > 23:

  print("Ingrese una hora entre 0 y 23")

  hora = (input("Ingrese hora de la llamada: "))



last_digit = round(((numero / 1000) - ((round(numero / 1000)) - 1)), 3)

first_digit = (round(numero / 100000)-1)





if hora > 0 and hora < 7:

  print("CONTESTAR")

elif hora < 14 and last_digit != 0.909:

  print("NO CONTESTAR")

elif hora < 14 and last_digit == 0.909:

  print("CONTESTAR")

elif hora >= 17 and hora <= 19 and first_digit != 877:

  print("CONTESTAR")

else:

  print("NO CONTESTAR")
      