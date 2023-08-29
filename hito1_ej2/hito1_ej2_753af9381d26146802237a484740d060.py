#Contestador de celular
NT = str(input("Ingresa un número telefonico de ocho dígitos: "))
H = int(input("Ingresa el registro de la hora en que ocurrió la llamada: "))
if(0 <= H <= 7):
  print("CONTESTAR")
elif(14 <= H <= 16):
  print("NO CONTESTAR")
elif(8 <= H <= 14):
  if str(NT[-3]) == "9" and str(NT[-2]) == "0" and str(NT[-1]) == "9":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif(17 <= H <= 19):
  if str(NT[-3]) == "8" and str(NT[-2]) == "7" and str(NT[-1]) == "7":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif(20 <= H):
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")
    