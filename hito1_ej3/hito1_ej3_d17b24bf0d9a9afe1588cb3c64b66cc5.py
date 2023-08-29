#Aprobación de créditos
I = int(input("Indique ingreso mensual en: "))
A = int(input("indique año de nacimiento: "))
N = int(input("indique número de hijos: "))
B = int(input("indique año de pertenencia al banco: "))
print("""
S: Soltero
C: Casado
""")
ECIVIL = input("indique la letra según corresponda: ")
print("""
U: Urbano
R: Rural
""")
C = input("indique si vive en campo o ciudad marcnado la letra correspondiente: ")
I1 = 2500000
I2 = 3500000
#print("Es: ", f"{I},{A}")

if(B>10 and N>=2):
    print("APROBADO")
elif (N>3 and ECIVIL == "C" and A>=1966 and A<=1976):
    print("APROBADO")
elif (I > I1 and ECIVIL == "S" and C == "U"):
    print ("APROBADO")
elif (I> I2 and B>5):
    print("APROBADO")
elif (C == "R" and ECIVIL == "C" and N<2):
    print("APROBADO")
else:
    print("RECHAZADO")      