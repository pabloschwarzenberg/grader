#Aprobación de créditos
W=int(input("Ingresos (En pesos): "))
X=int(input("Año de nacimiento: "))
Y=int(input("Numero de hijos: "))
Z=int(input("Años de pertenencia al banco: "))
print("Usted esta casado (C) o soltero (S) ")
seleccionó=input("Seleccione: ")
if seleccionó=="C":
    print("Usted esta casado.")
elif seleccionó=="S":
    print("Usted esta soltero.")
else:
    print("Opción no valida")
print("Usted vive en sitio urbano (U) o rural (R) ")
seleccionó=input("Seleccione: ")
if seleccionó=="U":
    print("Usted vive en un sitio urbano.")
elif seleccionó=="R":
    print("Usted vive en un sitio rural.")
else:
    print("Opción no valida")

if Z>10 and Y>2:
    print("APROBADO.")
elif Z==10 and Y==2:
    print("APROBADO")
else:
    print("RECHAZADO.")

if "C" and Y>3 and X>1976 and X<1966:
    print("APROBADO")
elif Y==3 and X>1976 and X<1966:
    print("APROBADO")
else:
    print("RECHAZADO")

if W>2500000 and "S" and "U":
    print("APROBADO")
elif W==2500:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if W>3500000 and Z>5:
    print("APROBADO")
elif W==3500000 and Z==5:
    print("APROBADO")
else:
    print("RECHAZADO")

if "R" and "C" and Y<2:
    print("APROBADO")
elif Y==2:
    print("APROBADO")
else:
    print("RECHAZADO")