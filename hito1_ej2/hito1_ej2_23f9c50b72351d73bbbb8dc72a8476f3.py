#Contestador de celular
numero=int(input("Ingrese el número de teléfono de 8 dígitos: "))
hora=int(input("Ingrese la hora de la llamada entre 0 y 23: "))

numero=str(numero)
terminacion=numero[5:8]
comienzo= numero[0:3]


if 0<=hora<=7:
  print("CONTESTAR")
elif 7<=hora<=14 and terminacion == "909":
  print("CONTESTAR")
elif 17<=hora<=19 and comienzo != "877":
  print("CONTESTAR")
else:
  print("NO CONTESTAR")

