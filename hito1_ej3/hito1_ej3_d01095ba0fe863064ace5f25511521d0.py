#Aprobación de créditos
ingresos=int(input())
nacimiento=int(input())
numero_hijos=int(input())
pertenencia_banco=int(input())
estado_civil=str(input())
campo_ciudad=str(input())
edad=2018-nacimiento
C=str("C")
S=str("S")
U=str("U")
R=str("R")
if pertenencia_banco>10 and numero_hijos>=2:
   print("APROBADO")
elif estado_civil==C and numero_hijos>3 and 45<edad<55:
   print("APROBADO")
elif ingresos>2500000 and estado_civil==S and campo_ciudad==U:
   print("APROBADO")   
elif ingresos>3500000 and pertenencia_banco>5:
   print("APROBADO")   
elif campo_ciudad==R and estado_civil==C and numero_hijos<2:
   print("APROBADO")   
else:
   print("RECHAZADO")