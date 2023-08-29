#Aprobación de créditos
ganancia=int(input("ingresos: ")) #ingresos en pesos
nacim=int(input("año de nacimiento: ")) #año de nacimiento
hijos=int(input("numero de hijos: ")) #numero de hijos
banco=int(input("años de pertenencia al banco: ")) #pertenencia al banco
estadoc=input("estado civil: ") #estado civil
lugar=input("donde vive: ") #lugar donde vive
U="U" or "u"
R="R" or "r"
S="S" or "s"
C="C" or "c"
anos=2020-nacim

if banco > 10 and hijos >=2:
    print("APROBADO")

if estadoc==C and hijos > 3 and 45<=anos<=55:
    print("APROBADO")

if ganancia > 2500000 and estadoc==S and lugar==U:
    print("APROBADO")

if ganancia > 3500000 and banco > 5:
    print("APROBADO")

if lugar==R and estadoc==C and hijos<2:
    print("APROBADO")