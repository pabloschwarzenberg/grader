#Aprobación de créditos
ingreso = input("Ingrese su Ingreso en pesos y sin puntos:")
ano_de_nacimiento =input("Ingrese si año de nacimiento:")
numero_de_hijos =input("Ingrese cuantos hijostiene:")
anos_de_pertenencia =input("Ingrese sus años de pertenencia al banco:")
estado_civil =input("Ingrese su estado civil S:soltero, C:casado;")
donde_vive = input("Ingrese donde vive U:urbano, R:rural:")
edad = 2020 - int(ano_de_nacimiento)
c=1
C=1
S=0
s=0
r=2
R=2
U=3
u=3
if int(anos_de_pertenencia) > 10 and int(numero_de_hijos) >= 2:
    print("APROBADO")
if estado_civil== c or C and int(numero_de_hijos) >= 3 and edad>45 and edad<55:
    print("APROBADO")
if int(ingreso)>2500000 and estado_civil == s or S and donde_vive==u or U:
    print("APROBADO")
if int(ingreso) > 3500000 and int(anos_de_pertenencia)>5:
    print("APROBADO")
if donde_vive == r or R and estado_civil == c or C and int(numero_de_hijos) <2:
    print("APROBADO")
