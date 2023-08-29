#Aprobación de créditos
# Entrada
a = int(input("Ingreso en pesos: "))
b = int(input("Año de nacimiento: "))
c = int(input("Numero de hijos: "))
d = int(input("Años de pertenencia en el banco: "))
e = str(input("Estado civil(S: soltero, C: casado): "))
f = str(input("Si vive en ciudad o campo(U: urbano, R: rural): "))

# Proceso
if d > 10 and c >= 2:
    credito="APROBADO"
    print(credito)
elif e == "C" and c > 3 and 1966 <= b <= 1976:
    credito="APROBADO"
    print(credito)
elif a > 2500000 and e == "S" and f == "U":
    credito="APROBADO"
    print(credito)
elif a > 3500000 and d > 5:
    credito="APROBADO"
    print(credito)
elif f == "R" and e == "C" and c < 2:
    credito="APROBADO"
    print(credito)
else:
    print("El credito es RECHAZADO por no cumplir los requisitos")