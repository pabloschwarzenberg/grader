ingresos=int(input())
nacimiento=int(input())
nhijos=int(input())
pertenencia=int(input())
estadocivil=input()
vive=input()

if pertenencia>10 and nhijos>1:
    print("APROBADO")
elif estadocivil=="C" and nhijos>3 and 1963<nacimiento<1973:
    print("APROBADO")
elif ingresos>2500000 and estadocivil=="S" and vive=="U":
    print("APROBADO")
elif ingresos>3500000 and pertenencia>5:
    print("APROBADO")
elif estadocivil=="C" and vive=="R" and nhijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      