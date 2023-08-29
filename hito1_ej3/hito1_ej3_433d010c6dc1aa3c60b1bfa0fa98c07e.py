#Aprobación creditos

ingreso=eval(input("¿Cuál es un ingreso?\n"))
año_nac=eval(input("Indiqueme su año de nacimiento:\n"))
num_hijos=eval(input("Indiqueme su cantidad de hijos:\n"))
años_banc=eval(input("Indiqueme cantidad de años siendo cliente de nuestro banco:\n"))
estado_civ=input("Estado civil:\n ""S"" Soltero\n ""C"" Casado\n")
hogar=input("¿En que zona vive?\n ""R"" Rural\n ""U"" Urbana\n")
C=""
S=""
R=""
U=""


if(años_banc>=10 and num_hijos>=2):
    print("APROBADO")
elif(estado_civ[0]==C and num_hijos>3 and año_nac>=1975 or año_nac<=1985):
    print("APROBADO")
elif(ingreso>2500000 and estado_civ[0]==S and hogar[0]==U):
    print("APROBADO")
elif(ingreso>3500000 and años_banc>5):
    print("APROBADO")
elif(hogar[0]==R and estado_civ[0]==C and num_hijos<2):
    print("APROBADO")
else:
    print("REPROBADO")