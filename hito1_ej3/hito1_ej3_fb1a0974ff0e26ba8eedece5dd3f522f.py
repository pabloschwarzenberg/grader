#Aprobación de créditos
ingreso=int(input("Ingreso:"))
nacimiento=int(input("Año de nacimiento:"))
hijos=int(input("Numero de hijos:"))
añosb=int(input("Años de pertenencia al banco:"))
estadoc=str(input("Estado civil:"))
residencia=str(input("Campo o ciudad:"))

años= 2016-nacimiento

if años>10 and hijos>=2:
    c1=True
else:
    c1=False

if estadoc=="C" and hijos>3 and 45<años<55:
    c2=True
else:
    c2=False

if ingreso>2500000 and estadoc=="S" and residencia=="U":
    c3=True
else:
    c3=False

if ingreso>3500000 and añosb>5:
    c4=True
else:
    c4=False

if residencia=="R" and estadoc=="C" and hijos<2:
    c5=True
else:
    c5=False

if c1==True or c2==True or c3==True or c4==True or c5==True:
    print("APROBADO")

else:
    print("RECHAZADO")
     