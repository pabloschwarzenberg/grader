#Aprobación de créditos
ingresos=eval(input("Ingrese pesos: "))
nacimiento=eval(input("Ingrese año de nacimiento: "))
hijos=eval(input("Ingrese cantidad de hijos: "))
pertenencia=eval(input("Ingrese años en el banco: "))
estado=input("Ingrese estado: ")
S="soltero"
C="casado"
sector=input("Ingrese sector: ")
U="urbano"
R="rural"

if(pertenencia>10 and hijos>2):
 print("APROBADO")

if(pertenencia<10 and hijos<2):
 print("RECHAZADO")
if(estado==C and hijos>3 and 1965<=nacimiento<=1975 ):
 print("APROBADO")

if(estado==R and 1965>=nacimiento>=1975 and hijos<3 ):
 print("RECHAZADO")

if(ingresos>2500000 and estado==S and sector==U):
 print("APROBADO")

if(ingresos<2500000 and estado==C and sector==R):
 print("RECHAZADO")

if(ingresos>3500000 and pertenencia>5):
 print("APROBADO")

if(ingresos<3500000 and pertenencia<5):
 print("RECHAZADO")

if(sector==R and estado==C or hijos<2):
 print("APROBADO")

if(sector==U and estado==S and hijos>2):
 print("RECHAZADO")     