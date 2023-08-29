#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
anos=int(input())
estado=input()
lugar=input()
if anos>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 45<=2017-nacimiento<=55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and lugar=="U":
    print("APROBADO")
elif ingreso>3500000 and anos>5:
    print("APROBADO")
elif lugar=="R" and estado=="C" and hijos<2:
    print("APROBADO")
    
else:
    print("RECHAZADO")