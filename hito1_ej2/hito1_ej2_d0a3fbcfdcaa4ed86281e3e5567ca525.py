# Contestador Automático
# Número telefonico
# Se ingresa un número
numero = int(input("Ingrese su número telefonico: "))
# Proceso del numero
while numero < 10000000 or numero >= 100000000:
  print("Número invalido")
  numero = int(input("Ingreso su número telefonico: "))
print("Número valido")

ultimos_digitos = numero % 1000
primeros_digitos = int(numero / 100000)

# Horario
hora = int(input("Ingrese la hora: "))
while hora < 0 or hora > 23:
  print("Horario incorrecto")
  hora = int(input("Ingrese la hora: "))
if (hora >= 0 and hora <= 7):
   print("CONTESTAR")
elif (hora >= 8 and hora <= 14):
  if ultimos_digitos == 909:
    print("CONTESTAR")
elif (hora >= 8 and hora <= 14):
  print("NO CONTESTAR")


    
elif (hora >= 15 and hora < 17):
  print("NO CONTESTAR")
elif (hora >=17 and hora <= 19):
  if primeros_digitos == 877:
    print("NO CONTESTAR")
elif (hora >=17 and hora <= 19): 
  print("CONTESTAR")
elif (hora > 19 and hora <= 23): 
  print ("NO CONTESTAR")