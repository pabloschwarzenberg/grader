#Aprobación de créditos
ingreso=int(input("Ingrese su ingreso en pesos:"))
yearNacimiento= int(input("Ingrese año de nacimiento: "))
numeroHijos=int(input("Ingrese número de hijos: "))
yearBanco=int(input("Ingrese años de pertenencia en el banco: "))
estadoCivil=input(("Si es soltero, ingrese S: ","Si es casado, ingrese C: "))
vive=input(("Si vive en una zona urbana, ingrese U: ","Si vive en una zona rural, ingrese R: "))
edad=2021-yearNacimiento
C=1
S=0
U=2
R=3

if(yearBanco>10 and numeroHijos>=2):
    print("CRÉDITO APROBADO")
elif(estadoCivil==1 and edad>=45 or edad<=55):
    print("CRÉDITO APROBADO")
elif(ingreso>2500000 and estadoCivil==0 and vive==2):
    print("CRÉDITO APROBADO")
elif(ingreso>3500000 and yearBanco>5):
    print("CRÉDITO APROBADO")
elif(vive==3 and estadoCivil==1 and numeroHijos<2):
    print("CRÉDITO APROBADO")
else:
    print("CRÉDITO RECHAZADO")
