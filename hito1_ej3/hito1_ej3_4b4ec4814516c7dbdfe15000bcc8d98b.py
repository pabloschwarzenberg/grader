ingreso=int(input("Ingrese su ingreso mensual en pesos: "))
anon=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese el numero de hijos que tiene: "))
anosp=int(input("Ingrese los años de pertenencia con el banco: "))
estado=str(input("Ingrese su estado civil, S=soltero, C=casado: "))
lugar=str(input("Ingrese lugar donde vive, U=urbano, R=rural: "))

if anosp>10 and hijos>=2:
    print("APROBADO")

elif estado=="C" and hijos>3 and 1961<=anon and 1971>=anon:
    print("APROBADO")
    
elif ingreso>=2500000 and estado=="S" and lugar=="U":
    print("APROBADO")
    
elif ingreso>=3500000 and anon>5:
    print("APROBADO")
   
elif lugar=="R" and estado=="C" and hijos<2:
    print("APROBADO")
    
else:
    print("REPROBADO")

