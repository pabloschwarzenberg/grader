#Contestador de celular
numero_telefono = str(input())
Hora = int(input())

if Hora >= 0 and Hora <= 7:
  print("CONTESTAR")

#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
if Hora < 14: 
  if numero_telefono[5:] == '909':
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877
if Hora > 17 and Hora < 19 : 
  if numero_telefono[:3] == '877':
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
#Después de las 19:00, no contestas el celular
if Hora > 19:
  print("NO CONTESTAR")