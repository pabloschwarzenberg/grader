#Aprobación de créditos
C=1
S=0
U=2
R=3
ingreso=float(input("ingrese su ingreso en Clp: "))
a_nacimiento=float(input("ingrese su año de nacimiento: "))
n_hijos=float(input("ingrese el numero de hijos: "))
a_pertenencia=float(input("ingrese la cantidad de años que usted pertenece al banco: "))
e_civil=input("ingrese su estado civil (S: soltero, C: casado): ")
vivienda=input("ingrese si vive en campo o ciudad (U: urbano, R: rural): ")


año=2021
edad=año-a_nacimiento
aprobado=False
if a_pertenencia>=10 and n_hijos>=2:
    aprobado=True
if e_civil==C and n_hijos>=3 and 45<=edad<=55:
    aprobado=True
if ingreso>=2500000 and e_civil==S and vivienda==U:
    aprobado=True
if ingreso>=3500000 and a_pertenencia>=5:
    aprobado=True
if vivienda!=C and e_civil!=R and n_hijos<2:
    aprobado=True



if aprobado==True:
    print("APROBADO")
if aprobado==False:
    print("RECHAZADO")
