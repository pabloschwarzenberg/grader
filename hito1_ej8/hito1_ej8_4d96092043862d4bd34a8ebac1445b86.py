numero = int(input("Ingrese un numero mayor a cero: "))
m = 0
c = 0
d = 0
u = 0
if numero//1000 > 0:
  m = numero//1000
  print("milesima", m)
if numero //100 > 0:
  c = numero//100 - m*10
  print("centesima", c)
if numero//10 > 0 :
  d = numero//10 - c*10 - m*100
  print("decima", d)
if numero//1 > 0:
  u = numero//1 - d*10 - c*100 - m*1000
  print("unidad", u)

      