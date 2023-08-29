#Aprobación de créditos
INGRESOS=float(input("Ingrese valor de sus ingresos: "))
A=int(input("Ingrese año de nacimiento: "))
HIJOS=int(input("Ingrese numero de hijos: "))
P=int(input("Ingrese años de pertenencia en el banco: "))
EC=input("Ingrese estado civil [S]oltero o [C]asado: ")
VIVE=input("Ingrese si vive en zona [R]ural o [U]rbana: ")

if A>10 and HIJOS>=2:
  print("APROBADO")
elif EC=="C" and HIJOS>3 and 45<=A<=55:
  print("APROBADO")
elif INGRESOS>2500000 and EC=="S" and VIVE=="U":
  print("APROBADO")
elif INGRESOS>3500000 and P>5:
  print("APROBADO")
elif VIVE=="R" and EC=="C" and HIJOS<2:
  print("APROBADO")
else:
  print("REPROBADO")
 
  