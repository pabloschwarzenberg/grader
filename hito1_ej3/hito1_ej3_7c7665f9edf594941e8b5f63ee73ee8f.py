ingresos=int(input("Ingrese sus ingresos: "))
ano=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
anosbanco=int(input("Ingrese sus años de pertenencia al banco: "))
estado=str(input("Ingrese su estado civil: "))
vive=str(input("¿Vive en la ciudad (U) o el campo (R)?: "))

if anosbanco>10 and 2<=hijos:
    print("APROBADO")
if estado.lower()=="c" and 3<hijos and 1976<ano<1966:
    print("APROBADO")
if 2500000<ingresos and estado.lower()=="C" and vive.lower()=="u":
    print("APROBADO")
if 3500000<ingresos and 5<anosbanco:
    print("APROBADO")
if vive.lower()=="r" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")

if vive.lower()=="r" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
