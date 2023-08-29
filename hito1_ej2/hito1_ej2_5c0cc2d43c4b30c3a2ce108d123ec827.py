#Contestador de celular
numero_telefono = int(input(" Ingrese numero telefonico: "))

horario = int(input(" Ingrese la hora de la llamada: "))

digitos_final = str(numero_telefono)[-3:]
digitos_inicial = str(numero_telefono)[:3]

if (horario>=0) and (horario<=7):
  print("CONTESTAR")

if (horario>7) and (horario<=14) and digitos_final !="909":
    print("NO CONTESTAR")
elif digitos_final == "909":
    print("CONTESTAR")
if (horario>=17) and (horario<=19) and digitos_inicial != "877":
  print("CONTESTAR")
elif digitos_inicial == "877":
    print("NO CONTESTAR")
if  (horario>19):
  print("NO CONTESTAR")      