I = int(input("Ingrese sus Ingresos en CLP: "))
A = int(input("Ingrese su Año de nacimiento: "))
N = int(input("Ingrese su Numero de Hijos: "))
P = int(input("Ingrese sus años de pertenencia al banco: "))
E = str(input("Ingrese su estado Civil de forma que, ´S´:Soltero y ´C´:Casado: "))
R = str(input("Ingrese si Vive en campo o ciudad de forma que, ´U´ Urbano y ´R´:Rural: "))

if (P >= 10) and (N >= 2):
    print("APROBADO")
elif (P < 10) and (N < 2):
    print("RECHAZADO")
elif (P < 10) and (N >= 2):
    print("RECHAZADO")
elif (P >=10) and (N < 2):
    print("RECHAZADO")


if (E=="C") and (N >= 3) and (A >=1966 <=1976):
    print("APROBADO")
elif (E=="S") and (N >= 3) and (A >=1966 <=1976):
    print("RECHAZADO")
elif (E=="C") and (N < 3) and (A >=1966 <=1976):
    print("RECHAZADO")
elif (E=="C") and (N >= 3) and (A <1966 >1976):
    print("RECHAZAR")
elif (E=="C") and (N < 3) and (A <1966 >1976):
    print("RECHAZADO")
elif (E=="S") and (N < 3) and (A >=1966 <=1976):
    print("RECHAZADO")
elif (E=="S") and (N >= 3) and (A <1966 >1976):
    print("RECHAZADO")
elif (E=="S") and (N < 3) and (A <1988 >1976):
    print("RECHAZADO")

if (I >= 2500000) and (E=="S") and (R=="U"):
    print("APROBADO")
elif (I < 2500000) and (E=="C") and (R=="R"):
    print("RECHAZADO")
elif (I < 2500000) and (E=="S") and (R=="U"):
    print("RECHAZADO")
elif (I >= 2500000) and (E=="C") and (R=="U"):
    print("RECHAZADO")
elif (I >= 2500000) and (E=="S") and (R=="R"):
    print("RECHAZADO")
elif (I < 2500000) and (E=="C") and (R=="U"):
    print("RECHAZADO")
elif (I < 2500000) and (E=="S") and (R=="R"):
    print("RECHAZADO")
elif (I >= 2500000) and (E=="C") and (R=="R"):
    print("RECHAZADO")

if (I >= 3500000) and (P >= 5):
    print("APROBADO")
elif (I < 3500000) and (P >= 5):
    print("RECHAZADO")
elif (I >= 3500000) and (P < 5):
    print("RECHAZADO")
elif (I > 3500000) and (P < 5):
    print("RECHAZADO")

if (R=="R") and (E=="C") and (N <= 2):
    print("APROBADO")
elif (R=="R") and (E=="C") and (N > 2):
      print("RECHAZADO")
elif (R=="R") and (E=="S") and (N <= 2):
    print("RECHAZADO")
elif (R=="U") and (E=="C") and (N <= 2):
    print("RECHAZADO")
elif (R=="R") and (E=="S") and (N > 2):
    print("RECHAZADO")
elif (R=="U") and (E=="C") and (N > 2):
    print("RECHAZADO")
elif (R=="U") and (E=="S") and (N <= 2):
    print("RECHAZADO")
elif (R=="U") and (E=="S")and (N > 2):
    print("RECHAZADO")
