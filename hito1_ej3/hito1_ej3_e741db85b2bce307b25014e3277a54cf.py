#Aprobación de créditos
a=int(input("Ingreso en pesos"))
b=int(input("Año de nacimiento"))
c=int(input("Numero de hijos"))
d=int(input("Años de pertenencia al banco"))
e=input("Estado civil" "S=soltero" "C=casado")
f=input("Campo o ciudad" "U=ciudad" "R=Campo")

if d>=10 and 2<=c:
   print ("APROBADO")
elif e=="C" and c>=3 and 45<=b<=55:
   print ("APROBADO")
elif a>=2500000 and e=="S" and f=="U":
   print ("APROBADO")
elif a>=3500000 and d>=5:
   print ("APROBADO")
elif f=="R" and e=="C" and c<=2:
   print ("APROBADO")
else:
   print ("RECHAZADO")

