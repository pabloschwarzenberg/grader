#Contestador de celular
Tel = int(input("Ingrese el número de teléfono:"))
if len(str(Tel)) != 8:
  print("Número no valido, valide que sean 8 digitos")
hora = int(input("Ingrese el horario:"))
dia = 24

if hora >= 0 and hora <=7:
  print("Contestar")

elif hora < 14:
  excep = str(Tel)[5:8]
  if excep == '909':
    print("contestar")
elif hora >= 17 and hora <= 19:
  excep = str(Tel)[0:3]
  if excep == '877':
    print ("No contestar")
elif hora > 19:
  print("No contestar")   