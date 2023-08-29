#Contestador de celular
NUM =  str(input("Ingrese su numero telefonico: "))
HORA = int(input("Ingrese hora de la llamada: "))

if HORA > 0 and HORA < 7:
  print("CONTESTAR")
if HORA > 19 and HORA <= 23:
  print("NO CONTESTAR")
else:
  if HORA > 7 and HORA < 14 and str(NUM[-3]) == "9" and str(NUM[-2]) == "0" and str(NUM[-1]) == "9":
    print("CONTESTAR")
  if HORA > 7 and HORA < 14 and str(NUM[-3]) != "9" and str(NUM[-2]) != "0" and str(NUM[-1]) != "9":
    print("NO CONTESTAR")
  if HORA > 17 and HORA < 19 and str(NUM[0:1]) == "8" and str(NUM[1:2]) == "7" and str(NUM[2:3]) == "7":
    print("NO CONTESTAR")
  if HORA > 17 and HORA < 19 and str(NUM[0:1]) != "8" and str(NUM[1:2]) != "7" and str(NUM[2:3]) != "7":
    print("CONTESTAR")