#Aprobación de créditos
ingreso=int(input()) #pesos
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
civil=str(input())
vive=str(input())
if pertenencia>=10 and hijos>=2:
    print("APROBADO")
if civil=="C" and hijos>3 and 1963<=nacimiento<=1973:
    print("APROBADO")
if ingreso>=2500000 and civil=="S" and vive=="R":
    print("APROBADO")
if ingreso>=3500000 and pertenencia>5:
    print("APROBADO")
if vive=="R" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
   
