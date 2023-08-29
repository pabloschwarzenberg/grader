#Aprobación de créditos
ing=int(input("¿Cuál es su ingreso en pesos?"))
nac=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("¿Cuántos hijos posee?"))
pert=int(input("¿Cuántos años de pertenecia presenta en la empresa?"))
sc=str(input("Si usted está soltero, ingrese una S. Si usted está casado ingrese una C"))
ur=str(input("Si vive en la ciudad ingrese una U. Si vive en el campo ingrese una R"))

edad=2018-nac

if (pert>=10 and hijos>=2)==True:
    print("APROBADO")
else:
    print("REPROBADO")

if (sc=="C" and hijos>=3 and 45<=edad<=55)==True:
    print("APROBADO")
else:
    print("REPROBADO")

if (ing>2500000 and sc=="S" and ur=="U")==True:
    print("APROBADO")
else:
    print("REPROBADO")

if (ing>3500000 and pert>5)==True:
    print("APROBADO")
else:
    print("REPROBADO")

if (ur=="R" and sc=="C" and hijos<2)==True:
    print("APROBADO")
else:
    print("REPROBADO")
