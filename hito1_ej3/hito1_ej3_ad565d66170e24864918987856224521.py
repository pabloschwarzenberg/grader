#Aprobación de créditos
I = int(input("Cual es su ingreso "))
A = int(input("Cual es su año de nacimiento "))
N = int(input("Cuantos hijos tiene "))
B = int(input("Cuantos años de pertenencia al banco tiene "))
E = input("Diga su estado civil S = Soltero, C = Casado ")
C = input("Usted vive en Campo = R, Ciudad = U ")

if B>=10 and N>=2:
    print("APROBADO")
elif E>="C" and N>3 and A>=1976 or A<=1966:
    print("APROBADO")
elif I>2500000 and E>"S" and C>"U":
    print("APROBADO")
elif I>3500000 and B>5:
    print("APROBADO")
elif C>"R" and E>"C" and N<2:
    print("APROBADO")
else:
    print("NO APROBADO")
