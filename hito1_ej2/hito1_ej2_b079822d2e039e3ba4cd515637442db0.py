#Contestador de celular
numero = eval(input("ingrese numero telefonico: "))
hora = eval(input("ingrese hora de llamada: "))
hora1 = 8
hora2 = 17
hora3 = 20
numero = str(numero)
fin = numero.endswith("909")
primer = numero.startswith("877")
if hora <= 7:
  print("contestar")
elif (hora1 <= 14):
  if (fin):
    print("contestar")
  else:
    print("no contestar")
  
elif (hora2 <= 19):
  if (primer):
    print("no contestar")
  else:
    print("contestar")
elif hora3 <= 23:
   print("no contestar")