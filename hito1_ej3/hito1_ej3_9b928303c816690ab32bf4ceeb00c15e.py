#Aprobación de créditos
A = int(input("Ingrece sus ingresos en pesos: "))
B = int(input("Ingrece su Año de nacimiento: "))
W = int(input("Ingrece Número de hijos: "))
D = int(input("Ingrece Años de pertenencia al banco: "))
E = (input("Ingrece su Estado civil (S = soltero, C = casado): "))
F = (input("Ingrece Si vive en campo o cuidad (U = urbano, R = rural): "))
C=E
c=E
S=E
s=E
U=F
u=F
R=F
r=F


Q = (2020 - B)

if (D>10) and (W>=2):
    print("APROBADO")
elif ((E==C) or (E==c)) and (W>3) and (45<=Q<=55):
    print("APROBADO")
elif (A>2500000) and ((E==S) or (E==s)) and ((F ==U) or (F==u)):
    print("APROBADO")
elif ((A>3500000) and (D>5)):
    print("APROBADO")
elif((F==R or F==r) and (E==C or E==c) and (W<2)):
    print("APROBADO")
else:
    print("RECHAZADO")
