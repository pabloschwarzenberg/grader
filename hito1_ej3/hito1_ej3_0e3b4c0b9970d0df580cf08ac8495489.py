#Aprobación de créditos
#Variables
ingreso=int(input("Favor de ingresar su ingreso mensual: "))
anona=int(input("Ingrese su año de nacimiento: "))
nhijos=int(input("Ingrese la cantidad de hijo que tenga: "))
anob=int(input("Ingrese años que pertenece usted al banco: "))
ecivil=str(input("Intrese su estado civil (S, soltero / C, casado): "))
vivienda=str(input("Ingrese tipo de recidencia (U, urbano / R, rural): "))

if anob>=10 and nhijos>=2:
    print("Su crédito fue APROBADO")
elif ecivil=="C" and nhijos>3 and anona>=1967 and anona<=1977:
    print("Su crédito fue APROBADO")
elif ingreso>=2500000 and ecivil=='S' and vivienda=='U':
    print("Su crédito fue APROBADO")
elif ingreso>=3500000 and anob>=5:
    print("Su crédito fue APROBADO")
elif nhijos<=2 and ecivil=='C' and vivienda=='R':
    print("Su crédito fue APROBADO")
else:
    print("Su crédito fue RECHAZADO")      