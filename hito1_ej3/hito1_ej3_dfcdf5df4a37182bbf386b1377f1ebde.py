ingreso=int(input())
año_nac=int(input())
hijos=int(input())
año_pert=int(input())
estado=input("")
localidad=input("")
edad=2017-año_nac
if año_pert>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and 45<=edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and localidad==U:
    print("APROBADO")
elif ingreso>3500000 and año_pert>5:
    print("APROBADO")
elif localidad=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZO")
    
