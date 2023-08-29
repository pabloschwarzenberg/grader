ingreso=int(input())
ano=int(input())
hijos=int(input())
pert=int(input())
estadocivil=input()
viveen=input()

casado="C"
soltero="S"
urbano="U"
rural="R"
if 10<pert and hijos>=2:
    print("APROBADO")
elif estadocivil==casado and hijos>3 and 45<=2017-ano<=55:
    print("APROBADO")
elif ingreso>3500000 and pert>5:
    print("APROBADO")
elif viveen==rural and estadocivil==casado and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")