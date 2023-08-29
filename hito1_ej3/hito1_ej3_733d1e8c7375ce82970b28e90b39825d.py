#Aprobación de créditos
#Entradas
ing=int(input("INGRESO: "))
nac=int(input("AÑO DE NACIMIENTO: "))
hijos=int(input("NÚMERO DE HIJOS: "))
años=int(input("AÑOS DE PRETENENCIA AL BANCO"))
ecivil=input("ESTADO CIVIL")
lugar=input("¿VIVE EN CAMPO O CIUDAD?: ")
#EDAD
edad=2020-nac
#CONDICIONES PARA APROBAR
if  años>10 and hijos>=2:
    print("APROBADO")
elif    ecivil=="C" and hijos>3 and (edad>=45 and edad<=55):
    print("APROBADO")
elif    ing>2500000 and ecivil=="S" and lugar=="U":
    print("APROBADO")
elif    ing>3500000 and años>5:
    print("APROBADO")
elif    lugar=="R" and ecivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")   