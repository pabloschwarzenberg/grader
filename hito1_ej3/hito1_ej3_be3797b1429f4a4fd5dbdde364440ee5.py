#Aprobación de creditos 
dinero=int(input("ingrese sus ingresos: "))
nacimiento=int(input("ingrese año de nacimiento: "))
hijos=int(input("numero de hijos: "))
pb=int(input("años de pertenencia al banco: "))
ec=input("s:soltero, c:casado. ")
cc=input("U:urbano , R:rural")
año=2022
edad=año-nacimiento

if pb>10 and hijos>=2:
    print("APROBADO")
    
if ec=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
    
if dinero>2500000 and ec=="S" and cc=="C":
    print("APROBADO")
    
if dinero>3500000 and pb>5:
    print("APROBADO")
    
if cc=="R" and ec=="C" and hijos <2:
    print("APROBADO")
    
else:
    print("RECHAZADO")
     
     