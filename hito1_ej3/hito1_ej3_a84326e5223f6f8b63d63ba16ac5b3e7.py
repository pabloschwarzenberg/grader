#Aprobación de créditos
ingreso=float(input("ingrese sus ingresos mensuales:"))
A=int(input("año de nacimiento:"))  
hijos=int(input("N° de hijos:"))
permanencia=int(input("años de permanencia en el banco:"))
estado_civil=input("estado civil;C-'casado',S-'soltero':")
donde_vive=("C-'campo', U-'urbano':")
años=A-2022
#DESARROLLO
if permanencia>10 and hijos>=2:
 print("APROBADO")
elif estado_civil=="C"and hijos>=1:
 print("APROBADO")