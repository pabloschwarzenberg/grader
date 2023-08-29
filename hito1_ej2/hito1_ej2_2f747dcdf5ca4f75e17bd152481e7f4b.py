#Contestador de celular
num = eval(input("Ingrese numero telefonico: "))
hor = eval (input("Ingrese hora de la llamada: "))
if hor >= 0 and hor <= 7:
  print("Resultado: CONTESTAR")
elif hor <= 14: 
  dig = num % 1000
  if dig == 909:
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif hor >= 17 and hor <= 19:
  dig = num // 100000
  if dig == 877:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif hor > 19:
  print("Resultado: NO CONTESTAR")