#Aprobación de créditos
ingresos=int(input())
nacimiento=int(input())
hijos=int(input())
pertencia=int(input())
estado=input()
vive=input()
if pertencia>=10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>=3 and nacimiento>=1975 and nacimiento<=1965:
    print("APROBADO")
elif ingresos>=2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingresos>=3500000 and pertenencia>=5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<=2:
    print("APROBADO")
else:
    print("REPROBADO")