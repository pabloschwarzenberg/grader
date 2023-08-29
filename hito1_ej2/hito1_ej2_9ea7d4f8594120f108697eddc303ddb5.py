#Contestador de celular
num = int(input("Ingrese número telefónico:"))
h = int(input("Ingrese hora de la llamada:"))
if h>19:
  resultado = "NO CONTESTAR"
elif h >= 17 and h <= 19:
  digits = list(str(num))
  first_3 = (digits[0],digits[1],digits[2])
  if first_3 == ('8','7','7'):
    resultado = "NO CONTESTAR"
  else:
    resultado = "CONTESTAR"
elif h > 7 and h <= 14:
  digits = list(str(num))
  last_3 = (digits[5],digits[6],digits[7])
  if last_3 == ('9','0','9'):
    resultado = "CONTESTAR"
  else:
    resultado = "NO CONTESTAR"
elif h<=7:
  resultado = "CONTESTAR"
  
print("Resultado:",resultado)      