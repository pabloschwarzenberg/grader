#Aprobación de créditos
I = int(input("Ingreso en pesos: "))
A = int(input("¿Año de nacimiento?: "))
N = int(input("¿Numero de hijos?: "))
B = int(input("¿Años de pertenencia en el banco?: "))
E = input("¿Estado civil? | Escriba S si está soltero | Escriba C si esta casado: ")
C = input("Si vive en el campo escriba R | Si vive en la ciudad escriba U: ")

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