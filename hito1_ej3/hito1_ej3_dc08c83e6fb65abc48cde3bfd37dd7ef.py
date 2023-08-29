#Aprobación de créditos
ingreso=float(input("ingrese su ingreso mensual: "))
nacimiento=int(input("ingrese su año de nacimiento: "))
hijos=int(input("Ingrese el numero de hijos que tiene: "))
año_lealtad=float(input("ingrese cuanto tiempo (en años) ha pertenecido a este banco: "))
estado=input("ingrese su estado civil {} si es soltero o {} si es casado: ".format("S","C"))
residencia=input("ingrese {} si vive en el campo o {} si vive en la cuidad: ".format("R","U"))
if año_lealtad>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 1963>nacimiento>1973:
    print("APROBADO")
elif ingreso>2.5*10**5 and estado=="S" and residencia=="U":
    print("APROBADO")
elif ingreso>3.5*10**5 and año_lealtad>5:
    print("APROBADO")
elif residencia=="R" and estado=="C" and 2>hijos:
    print("APROBADO")
else:
    print("RECHAZADO")
                   