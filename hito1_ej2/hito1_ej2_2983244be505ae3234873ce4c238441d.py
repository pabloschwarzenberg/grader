#Contestador de celular
nro=int(input("ingrese su numero(8 cifras): "))
hr=eval(input("ingrese la hora de llamada: "))
if 10000000<=nro<=99999999 and 0<=hr<=23:
  if 0<=hr<=7:
    print("CONTESTAR")
  if 7<=hr<=14 and nro%1000!=909:
    print("NO CONTESTAR")
  if 7<=hr<=14 and nro%1000==909:
    print("CONTESTAR")
  if 15<=hr<=17:
    print("NO CONTESTAR")
  if 17<=hr<=19 and nro//100000!=877:
    print("CONTESTAR")
  if 17<=hr<=19 and nro//100000==877:
    print("NO CONTESTAR")
  if 19<hr<=23:
    print("NO CONTESTAR")