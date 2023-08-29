#Aprobación de créditos
from datetime import datetime
now = datetime.now()
ingreso= int(input("Ingrese su ingreso en pesos: "))
anacimiento = int(input("Ingrese su año de nacimineto: "))
nhijos=int(input("Ingrese su numero de hijos: "))
abanco=int(input("Ingrese años de pertenencia al banco: "))
ecivil=input("Ingrese su estado civil(S/C): ")
residencia=input("Ingrese su residencia(U/R): ")
edad= now.year-anacimiento
if abanco> 10 and nhijos>=2:
    print("Credito APROBADO")
elif ecivil.upper() == "C" and nhijos>3 and (edad>=45 and edad<=55):
    print("Credito APROBADO")
elif (ingreso > 2500000) and ecivil.upper()=="S" and residencia.upper()=="U":
    print("Credito APROBADO")
elif ingreso > 3500000 and abanco>5:
    print("Credito APROBADO")
elif residencia.upper()=="R" and ecivil.upper()=="C" and nhijos<2:
    print("Credito APROBADO")
else:
    print("Credito RECHAZADO")
