#Aprobación de créditos
i = int(input("Ingrese sus ingresos(pesos):"))
a = int(input("Ingrese año de nacimiento:"))
h = int(input("ingrese numero de hijos:"))
ab = int(input("ingrese años de pertenencia con el banco:"))
ec = str(input("ingrese, S = soltero, C = casado:"))
v = str(input("ingrese U = urbano, R = rural:"))
x = 2021-a

if ab > 10 and h >= 2: 
   print("APROBADO")

elif ec.upper()=="C" and h > 3 and x >= 45 and x <=55:
   print("APROBADO")
   
elif i > 2500000 and ec.upper()=="S" and v.upper()=="U":
   print("APROBADO")
   
elif i > 3500000 and ab > 5:
   print("APROBADO")
   
elif v.upper()=="R" and ec.upper()=="C" and h < 2:
   print("APROBADO")
      
else:
   print("RECHAZADO")