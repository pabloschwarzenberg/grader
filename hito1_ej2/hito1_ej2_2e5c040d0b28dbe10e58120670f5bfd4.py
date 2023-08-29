#Contestador de celular
numero = eval(input("ingrese numero:"))
hora = eval(input("ingrese hora de la llamada:"))

if hora >= 0 and hora <=7:
  print("Resultado:CONTESTAR")
elif hora <=14:
  digitos = numero % 1000
  if digitos == 909:
   print("Resultado:CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif hora >= 17 and hora <= 19:
  digitos = numero // 100000
  if digitos == 877:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif hora > 19:
  print("Resultado: NO CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")