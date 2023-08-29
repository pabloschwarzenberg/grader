#Aprobación de créditos
P=int(input("Ingreso (en pesos):"))
N=int(input("Año de nacimiento:"))
H=int(input("número de hijos:"))
A=int(input("Años de pertenencia al banco:"))
E=input("Estado civil S:soltero, C:casado:")
Z=input("Zona de vivienda U:urbano y R:rural:")

edad=(2021-N)

if A>10 and H>=2:
    print("APROBADO")
elif E == "C" and (H>3) and (EDAD>45) and (EDAD<55):
    print("APROBADO")
elif P>2500000 and (E=="S") and (Z=="U"):
    print("APROBADO")
elif P>3500000 and (A>5):
    print("APROBADO")
elif Z == "R" and E=="C" and H<2:
    print("APROBADO")
else:
    ("no apto, Bienvenido a chile")    