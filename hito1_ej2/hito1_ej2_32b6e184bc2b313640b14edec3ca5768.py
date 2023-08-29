#Contestador de celular
#LLAMADA ENTRANTE, INPUT NÚMERO Y HORA
nm=int(input("Número de teléfono entrante: "))
nmi=nm//100
nmf=nm%100000
hr=int(input("Hora de la llamada entrante: "))
#EVALUACIÓN
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
if hr>19:
  print("NO CONTESTAR")
else:
  if 19>=hr>=17 and nmi!=877:
    print("NO CONTESTAR")
  else:
    if 0<hr<7:
      print("CONTESTAR")
    else:
      if hr<14:
        if hr<14 and nmf==909:
          print("NO CONTESTAR")
        else:
          print("CONTESTAR")

  