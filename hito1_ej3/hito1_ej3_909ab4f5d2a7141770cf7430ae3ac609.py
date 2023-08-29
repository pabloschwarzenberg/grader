1 #Creditos:
ingreso=float(input("ingrese sus ingresos mensuales:"))
A=int(input("Año de nacimiento:"))
hijos=int(input("N° de hijos: "))
APB=float(input("Años de pertenecia en el banco: "))
EC=input("Estado civil: C+ casado', S-'soltero':")
AM=input("en que entorno vive; C-'Campo', U-'Urbano':")
años=A-2022
EU= EC.upper()
 #desarrollo.
if APB>18 and hijos>=2:
 print("APROBADO")
elif EC.upper()=="C" and hijos>3 and años>=45 and años<=55:
  print("APROBADO")
 elif ingreso>2500000 and EC=='S' and AM=='U':
  print("aprobado")
elif ingreso>3500000 and APB>5: 
  print("aprobado")
elif AM=='R' and EC=='C' and hijos<=2:
  print("aprobado")
else:
  print("rechazado")