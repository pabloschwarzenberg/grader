#Aprobación de créditos
ingreso= int(input())
nacimiento= int(input())
hijos= int(input())
anos= int(input())
estado= str(input())
zona= str(input())

if (ingreso>2500000)and(estado=="S")and(zona=="U"):
   print("APROBADO")
elif (estado=="C")and(hijos>3)and(45<(2017- nacimiento)<55):
   print("APROBADO")
elif (ingreso>3500000)and(anos>5):
   print("APROBADO")
elif (anos>10)and(hijos>=2):
   print("APROBADO")
elif (zona=="R")and(estado=="C")and(hijos<2):
   print("APROBADO")
else:
   print("RECHAZADO")