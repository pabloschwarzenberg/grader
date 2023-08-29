#Aprobación de créditos
print("cual es su ingreso?: ")
ingreso= float(input("$"))
print("cual es su año de nacimiento")
añodenacimiento=int(input())
print("cuantos hijos tiene? ")
hijos=int(input())
print("cuanto tiempo lleva en el banco? ")
añosenelbanco=int(input())
print("Estado civil (S:soltero, C:casado) ")
estadocivil=input()
print("vive en campo o cuidad (U:urbano, R:rural)")
vive=input()
if añosenelbanco > 10 and hijos >= 2:
    print("APROBADO")
if estadocivil=="C" and hijos >3 and añodenacimiento in range(1966, 1976):
    print("APROBADO")
if ingreso >= 2500000 and estadocivil=="S"  and vive=="U":
    print("APROBADO")
if ingreso> 3500000 or añosenelbanco >5:
    print("APROBADO")
if vive== "R" and estadocivil=="C" and hijos<=2:
    print("APROBADO")
else:
    print("RECHAZADO")
   