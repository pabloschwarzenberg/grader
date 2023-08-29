#Aprobación de créditos
ingreso=int(input("cuanto ganai"))
nacimiento=2016-int(input("cuando naciste"))
hijos=int(input("cuandos hijos"))
años=int(input("cuantos años te hemos timado"))
estado=input("S: soltero, C: casado")
lugar=input("U: urbano, R: rural")

if años>10 and hijos>=2:
    print("APROBADO")
if "S" in estado and hijos>3 and 45>nacimiento>55:
    print("APROBADO")
if ingreso>2500000 and "S" in estado and "U" in lugar:
    print("APROBADO")
if ingreso>3500000 and años>5:
    print("APROBADO")
if "R" in lugar and "C" in estado and hijos<2:
    print("APROBADO")