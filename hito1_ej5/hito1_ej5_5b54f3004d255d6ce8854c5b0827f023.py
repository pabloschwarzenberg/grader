rut =int(input("Ingrese su rut sin puntos ni guion: "))
d8 = (rut % 10)
d7 = (rut % 100)
d7 = int(d7 / 10)
d6 = (rut % 1000)
d6 = int(d6 / 100)
d5 = (rut % 10000)
d5 = int(d5 / 1000)
d4 = (rut % 100000)
d4 = int(d4 / 10000)
d3 = (rut % 1000000)
d3 = int(d3 / 100000)
d2 = (rut % 10000000)
d2 = int(d2 / 1000000)
d1 = (rut % 100000000)
d1 = int(d1 / 10000000)

suma = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 + d2*2 + d1*3
division = int(suma/11)
entero = int(suma - division*11)
digito = int(11 - entero)
if digito == 11:
  print("dv = 0") 
elif digito == 10:
  print("dv = k")
elif (digito >=0) and (digito <= 9):
  print("dv =",digito) 