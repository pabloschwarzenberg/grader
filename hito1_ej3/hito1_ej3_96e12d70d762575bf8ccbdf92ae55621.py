#Aprobación de créditos

ingresos=int(input("ingresos: ")) #ingresos en pesos
anonac=int(input("año de nacimiento: ")) #año de nacimiento
numhij=int(input("numero de hijos: ")) #numero de hijos
pertbanc=int(input("años de pertenencia al banco: ")) #pertenencia al banco
estciv=input("estado civil: ") #estado civil
vive=input("donde vive: ") #lugar donde vive
U="U" or "u"
R="R" or "r"
S="S" or "s"
C="C" or "c"
anos=2020-anonac

if pertbanc > 10 and numhij >=2:
    print("APROBADO")

if estciv==C and numhij > 3 and 45<=anos<=55:
    print("APROBADO")

if ingresos > 2500000 and estciv==S and vive==U:
    print("APROBADO")

if ingresos > 3500000 and pertbanc > 5:
    print("APROBADO")
    
if vive==R and estciv==C and numhij<2:
    print("APROBADO")