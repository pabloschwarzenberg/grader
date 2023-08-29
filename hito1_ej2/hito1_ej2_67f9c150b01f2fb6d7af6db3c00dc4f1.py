#Contestador de celular
Numero = int(input("Ingrese numero telefonico:"))
Hora = int(input("Ingrese hora de la llamada:"))
if Hora>=0 and Hora<=7:
  Resultado = print("CONTESTAR")
elif (7<Hora<=14):
  if Numero %1000 ==909:
    Resultado = print("CONTESTAR")
  else:
    Resultado = print("NO CONTESTAR")
elif 17<=Hora<=19:
  if str(Numero).startswith('877'):
    Resultado = print("NO CONTESTAR")
  else:
    Resultado = print("CONTESTAR")
elif Hora>=19:
  Resultado = print("NO CONTESTAR")

print(Resultado)
    