ingreso=eval(input("ingrese su ingreso en pesos :"))
anios= eval(input("ingrese su año de nacimiento:"))
numero_hijos=eval("Ingrese cuantos hijos tiene :")
anios_banco=eval(input("Ingrese cuantos añoa lleva en el banco :"))
estado_civil=(input("Si es soltero,ingrese S,si es casado ingrese C:"))
casado=str("C")
soltero=str("S")
lugar=(input("si vive en campo ingrese R,si vive en ciudad ingrese U:"))
ciudad=str("U")
campo=str("R")
if anios_banco>10 and numero_hijos>2 :
    print("APROBADO")
    
if estado_civil==casado and numero_hijos>3 and anios <=1966 and aios >=1956:
    print("APROBADO")
    if ingreso>2500000 and estado_civil==soltero and lugar ==ciudad :
        print("APROBADO")

if ingreso >3500000 and anios_banco>5:
    print("APROBADO")

if lugar== campo and estado_civil== casado and numero_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")