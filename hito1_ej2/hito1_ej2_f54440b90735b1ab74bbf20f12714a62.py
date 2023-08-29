#Contestador de celular
# Ingresar el numero que llama y la hora a la que llama y (darle limite)
numero = input("Ingrese el numero telefonico: ")
hora = input("Ingrese la hora a la que llama: ")

# Agregar las condiciones del programa, ejemplo hora 00:00 hasta 07:00 se contesta.
if 0 <= int(hora) <= 7:
  print("CONTESTAR")
    
# Tiene que cumplir dos condiciones para contestar.
if 8 <= int(hora) <= 14 and numero[5:8] == str(909):
  print("CONTESTAR")
if 8 <= int(hora) <= 14 and numero[5:8] != str(909):
  print("NO CONTESTAR")

# De las 17 a las 19 contesto excepto a 877...
if 17 <= int(hora) <= 19 and numero[0:3] == str(877):
  print("NO CONTESTAR")
if 17 <= int(hora) <= 19 and numero[0:3] != str(877):
  print("CONTESTAR")

# Despues de la 7 de la tarde no se contesta
if 20 <= int(hora) <= 23:
  print("NO CONTESTAR")