#Aprobación de créditos
Ingreso=int(input())
Agno=int(input())
NH=int(input())
Pert=int(input())
EC=input("")
CoC=input("")
edad=2017-Agno

if Pert>10 and NH>=2:
    print("APROBADO")
elif EC=="C" and NH>3 and 45<edad<55:
    print("APROBADO")
elif 2500000<Ingreso<3500000 and EC=="S" and CoC=="U":
    print("APROBADO")
elif Ingreso>3500000 and Pert>5:
    print("APROBADO")
elif CoC=="R" and EC=="C" and NH<2:
    print("APROBADO")
else:
    print("NO APROBADO")