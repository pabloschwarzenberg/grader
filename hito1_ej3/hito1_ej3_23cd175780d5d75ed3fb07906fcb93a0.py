#Aprobación de créditos
ingreso=int(input("Su ingreso es: "))
nacimiento=int(input("Ingrese año de nacimiento"))
hijos=int(input("Ingrese la cantidad de hijos: "))
antiguedad=int(input("Ingrese los años de pertenencia al banco: "))
ec=input("Ingrese su estado civil (S : soltero, C: casado, mayusculas): ")
zona=input("Indique si vive en campo o cuidad (U: urbano, R: rural, mayusculas): ")

if((antiguedad>10 and hijos>=2) or (ec=='C' and hijos>3 and 44<edad<55) or (ingreso>2500000 and ec=='S' and zona=='U') or (ingreso>3500000 and antiguedad>=5) or (zona=='R' and ec=='C' and hijos<2)):
   print("APROBADO")
else:
   print("Rechazado")