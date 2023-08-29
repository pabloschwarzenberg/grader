#Aprobación de créditos
ingresos=int(input("ingresos: ")) 
fechaNacimiento=int(input("año de nacimiento: ")) 
hijos=int(input("numero de hijos: ")) 
anoPertencia=int(input("años de pertenencia al banco: ")) 
estadoCivil=input("estado civil: ") 
residencia=input("donde vive: ") 
U="U" or "u"
R="R" or "r"
S="S" or "s"
C="C" or "c"
anos= 2020-fechaNacimiento

if anoPertencia > 10 and hijos >=2:
    print("APROBADO")

if estadoCivil ==C and hijos > 3 and 45<=anos<=55:
    print("APROBADO")

if ingresos > 2500000 and estadoCivil==S and vive==U:
    print("APROBADO")

if ingresos > 3500000 and anoPertencia > 5:
    print("APROBADO")

if residencia==R and estadoCivil==C and hijos<2:
    print("APROBADO")  