#Aprobación de créditos
I=int(input("Ingrese sus ingresos:"))
A=int(input("Ingrese su año de nacimiento:"))
H=int(input("Ingrese su número de hijos:"))
P=int(input("Ingrese sus años de pertenencia al banco"))
E=input("Ingrese su esrtado civil:")
if (bool(E=="C"))==True:
  E=1
else:
  E=0
V=input("Ingrese si lugar de vivienda:")
if (bool(V=="U"))==True:
  V=1
else:
  V=0
if (bool(P>=10))==True  and (bool(H>=2))==True:
  print("APROBADO")
elif bool(E==1)==True and H>=3==True and 45<=2017-A<=55==True:
    print("APROBADO")
elif (bool(I>=250000))==True and (bool(E==0))==True and (bool(V==1))==True:
   print(APROBADO)
elif bool(H<=19)==True:
   print("APROBADO")
else:
   print("RECHAZADO")
     