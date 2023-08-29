ingreso=int(input("ingresos: "))
yearn=int(input("nacimiento:"))
nhijos=int(input("numero de hijos:"))
yearbanco=int(input("year perteneciente al bacno:"))
ec=input("estado civil:")
ur=input("Campo o ciudad ")
A=0
R=0
print (yearn)
if yearbanco>9 and nhijos>1:
    A=1
if ec==("C") and nhijos>3 and (yearn>1974 and yearn<1986):
    A=1
if ingreso>2500000 and ec==("S") and ur==("U"):
    A=1
if ingreso>3500000 and yearbanco>5:
    A=1
if ur==("R") and ec==("C") and nhijos<2:
    A=1
    
    
    
if A>R:
    print ("APROBADO")
else:
    print ("RECHAZADO")

