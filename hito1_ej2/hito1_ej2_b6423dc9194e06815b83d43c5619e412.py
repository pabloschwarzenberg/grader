#Contestador de celular
n=int(input("Ingrese su número de teléfono de 8 dígitos: "))
h=int(input("Ingrese la hora de la llamada entre las 00 y 23: "))
x=n/1000
y=str(x).split(".")
z=int(y[1])
if(h>=17 and h<=19 and n>=87700000 and n<=87799999 or h>=20 and h<=23):
  print("NO CONTESTAR")
else:
  if(h>=00.0 and h<=07.0 or h>=17.0 and h<=19.0 or h>07.0 and h<14.0 and z==909):
    print("CONTESTAR")
