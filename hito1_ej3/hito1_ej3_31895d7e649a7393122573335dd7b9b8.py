I=int(input("ingreso"))
A=int(input("año de nacimiento"))
N=int(input("numero de hijos"))
A_P=int(input("años de pertenencia"))
E=str(input("estado civil(S= soltero, C= casado"))
UR=str(input("Si vive en campo o cuidad (U= urbano, R= rural"))

EDAD= (2021 - A)

if(A> 10 and N>= 2)or (E == "C" and N > 3 and EDAD>=45 and EDAD<=55)or (I>= 2500000 and E == "S" and UR == "U") or (I>= 3500000 and A_P >= 5) or (UR == "R" and E == "C" and N < 2):
    print("APROBADO1")
    

#if(E == "C" and N > 3 and EDAD>=45 and EDAD<=55):
   # print("APROBADO2")


#if(I>= 2500000 and E == "S" and UR == "U"):
   # print("APROBADO3")


#if(I>= 3500000 and A_P >= 5):
   # print("APROBADO4")


#if(UR == "R" and E == "C" and N >= 2):
    # print("APROBADO5")
    

else:
    print("RECHAZADO")
